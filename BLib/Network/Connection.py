import socket
import os
from BLib.Strings.Convert import sanitize, ListToString
from BLib.Files.ReadWrite import GetLinesAsList
from BLib.Network.Formatting import RemoveNullTerminator



class Connection:
    def __init__(self, ip, port, buffer=1024):
        self.buffer = buffer
        self.s = socket.socket()
        self.ip = ip
        self.port = port

        self.s.connect((ip, port))

    def Send(self, message):
        self.s.send(bytes(message, 'UTF-8'))

    def RecieveNoSanitize(self):
        return self.s.recv(self.buffer)

    def Recieve(self):
        return sanitize(self.s.recv(self.buffer))

    def WaitUntilRecv(self, message=None, format_incoming=None, log=False):
        specific_message = message is not None
        while True:
            d = self.RecieveNoSanitize()
            if log:
                print(f'Expected: {message}')
            if not d == '':
                d = sanitize(d)
                if format_incoming is not None:
                    d = format_incoming(d)
                if log:
                    print(f'Got: {d}')
                if specific_message and d == message:
                    break
                elif not specific_message:
                    break
                else:
                    continue
        return d

    def Close(self):
        self.s.close()
        del self


    #contcode: what to send to the other end to continue recieving data
    #stopcode: the string that represents the end of the datastream
    def RecvList(self, contcode, stopcode):
        
        stuff = []
        
        done = False

        while not done:
            data = self.s.recv(self.buffer)
            self.Send(contcode)
            if sanitize(data) == stopcode:
                done = True
                break
            elif not data == b'':
                stuff += [sanitize(data)]
                
        return stuff
    
    def RecvFile(self, filename, contcode, endcode, replace=False):
        if os.path.exists(filename) and replace:
            os.remove(filename)
        elif os.path.exists(filename) and not replace:
            raise FileExistsError(f"'{filename}' already exists!")
        
        s = self.RecvList(contcode, endcode)
        
        f = open(filename, 'w+')
        
        d = ListToString(s, '\n')
        
        f.write(d)
        
        f.close()
        
    def SendList(self, contcode, endcode, lst, from_cpp=False):
        if from_cpp:
            func = RemoveNullTerminator
        else:
            func = None
        for i in lst:
            self.Send(i)
            self.WaitUntilRecv(message=contcode, format_incoming=func)
            
        self.Send(endcode)

    def SendFile(self, contcode, endcode, filename):

        if not os.path.exists(filename):
            raise FileNotFoundError(f"'{filename}' not found")
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"'{filename}' is a directory")

        to_send = GetLinesAsList(filename, include_newlines=False)

        self.SendList(contcode, endcode, to_send)

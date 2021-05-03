import os
import socket

from BLib.Files.ReadWrite import get_lines_as_list
from BLib.Network.Formatting import remove_null_terminator
from BLib.Strings.Convert import sanitize, ListToString


class Connection:
    def __init__(self, ip, port, buffer=1024):
        self.buffer = buffer
        self.s = socket.socket()
        self.ip = ip
        self.port = port

        self.s.connect((ip, port))

    def send(self, message):
        self.s.send(bytes(message, 'UTF-8'))

    def receive_no_sanitize(self):
        return self.s.recv(self.buffer)

    def receive(self):
        return sanitize(self.s.recv(self.buffer))

    def wait_until_recv(self, message=None, format_incoming=None, log=False):
        specific_message = message is not None
        while True:
            d = self.receive_no_sanitize()
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

    def close(self):
        self.s.close()
        del self

    def recv_list(self, contcode, stopcode):

        stuff = []

        done = False

        while not done:
            data = self.s.recv(self.buffer)
            self.send(contcode)
            if sanitize(data) == stopcode:
                done = True
                break
            elif not data == b'':
                stuff += [sanitize(data)]

        return stuff

    def recv_file(self, filename, contcode, endcode, replace=False):
        if os.path.exists(filename) and replace:
            os.remove(filename)
        elif os.path.exists(filename) and not replace:
            raise FileExistsError(f"'{filename}' already exists!")

        s = self.recv_list(contcode, endcode)

        f = open(filename, 'w+')

        d = ListToString(s, '\n')

        f.write(d)

        f.close()

    def send_list(self, contcode, endcode, lst, from_cpp=False):
        if from_cpp:
            func = remove_null_terminator
        else:
            func = None
        for i in lst:
            self.send(i)
            self.wait_until_recv(message=contcode, format_incoming=func)

        self.send(endcode)

    def send_file(self, contcode, endcode, filename):

        if not os.path.exists(filename):
            raise FileNotFoundError(f"'{filename}' not found")
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"'{filename}' is a directory")

        to_send = get_lines_as_list(filename, include_newlines=False)

        self.send_list(contcode, endcode, to_send)

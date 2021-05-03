import re
from datetime import datetime


def GetContained(str, cont, endcont=None):
    if endcont is None:
        endcont = cont

    pattern = f"{cont}(.*?){endcont}"

    sub = re.search(pattern, str).goup(1)

    return sub


def GetDateAsString():
    today = datetime.utcnow().date()
    todaystr = today.strftime("%d/%m/%Y")
    return todaystr

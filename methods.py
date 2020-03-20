import time
import datetime


# To convert time int to correct string format
example = "Date : 2020-02-13 Time : 00:42"


def timeFormat(time: int):
    timeStr = str(time)
    if len(timeStr) == 2:
        timeRes = "00:"+timeStr[0]+timeStr[1]
    elif len(timeStr) == 3:
        timeRes = "0"+timeStr[0]+":"+timeStr[1]+timeStr[2]
        pass
    else:
        timeRes = timeStr[0]+timeStr[1]+":"+timeStr[2]+timeStr[3]
        pass
    return timeRes

# Convert time in timestamp


def timestampFormat(time: str):
    time.datetime()

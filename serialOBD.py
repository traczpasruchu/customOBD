import serial
import time

responseFound = False

cmdList = ['ATE0\r', 'ATH1\r', 'ATL0\r', '0100\r']


def readline(char="\r"):
    out = bytes("", "utf-8")
    b = ""

    while b != bytes(char, "utf-8"):
        b = ser.read()
        out += b

    return out


def readlines(char="\r"):
    outList = []
    l = ""

    while l != bytes(char, "utf-8"):
        l = readline()
        outList.append(l)

    return outList

def run(cmd):
    ser.write(bytes(cmd + "\r", "utf-8"))
    readline()


def runAndReturn(cmd, char="\r"):
    ser.write(bytes)


ser = serial.Serial("COM3", 9600, xonxoff=True)
"""
print("serial opened")
for i in cmdList:
    ser.write(bytes(i, "utf-8"))
    print(readline("\r"))
    time.sleep(0.5)

#s = readline("\r")
ser.close()

#print(s)
"""
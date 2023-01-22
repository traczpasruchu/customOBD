import obd
import time
import os
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_hex

connection = obd.OBD("COM7")    # Open asynchronous OBD-II connection


# This function will run as a callback every time a new value is found
def new_rpm(r):
    print(r)


def rpm(messages):
    d = messages[0].data
    print(bytes_to_hex(d))
    supp = ""
    for i in d[-4:]:
        print(bin(i))
        supp += str(bin(i)[2:])
    print(len(supp))
    for i in range(len(supp)):
        pidNum = str(hex(i + 1))[2:].zfill(2)
        print("PID " + pidNum + " is ", end="")
        if supp[i] == "1":
            print("supported")
        else:
            print("not supported")
    d = d[2:]
    return d


myCMD = OBDCommand("RPM", "Engine RPM", b"0100", 6, rpm, ECU.ENGINE, True)

response = connection.query(myCMD, force=True)

connection.close()

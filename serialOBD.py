import serial
import time

responseFound = False

cmdList = ['ATZ\r', 'ATE0\r', 'ATH1\r', '0100\r']

ser = serial.Serial("COM7", 9600, xonxoff=True)
for i in cmdList:
    ser.write(bytes(i, "utf-8"))
    time.sleep(0.5)

s = ser.readlines(10)
ser.close()

print(s)

import obd
import time
import os

os.system("\"C:\\Program Files (x86)\\Bluetooth Command Line Tools\\bin\\btcom.exe\" -b8C:DE:00:02:4E:EA -c")
connection = obd.Async("COM3")    # Open asynchronous OBD-II connection


# This function will run as a callback every time a new value is found
def new_rpm(r):
    print(r.value)


connection.watch(obd.commands.RPM, callback=new_rpm)    # Subscribe RPM command to updates with a callback
connection.start()  # Start the update loop

time.sleep(15)      # Let the udpate loop run for 1 minute
connection.stop()   # Stop the update loop

connection.close()
os.system("\"C:\\Program Files (x86)\\Bluetooth Command Line Tools\\bin\\btcom.exe\" -b8C:DE:00:02:4E:EA -r")

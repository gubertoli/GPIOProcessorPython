#
# Linker Mezzannine Board - RF (HC-12) x UART
#
# Required python-serial:
#   pip install pyserial
#   easy_install -U pyserial
#


import serial, time
from datetime import datetime
from GPIOProcessor import GPIOProcessor

# HC-12 Configuration
# Using UART port from Linker Sprite Mezzanine
ser = serial.Serial('/dev/tty96B1',baudrate=9600)
time.sleep(2)

GP = GPIOProcessor()
                            # Port D4 from Linker Sprite Mezzanine (D_G)
SETPin = GP.getPin29()      # HC-12 SET Pin connected to DB410C LS pin 29

SETPin.out()                # Defined as output
print ">> SET PIN ---> " + SETPin.getDirection()
print ">> SET PIN ---> LOW (AT Command)"
SETPin.low()                # Enter to AT Command
print ">> HC-12 Set to Default (FU3 / 9600bps / CH1 433.4MHz)"
ser.write("AT+DEFAULT")     # SET HC-12 Default Configuration
time.sleep(2)
SETPin.high()               # Enter Transparent Mode
print ">> SET PIN ---> HIGH (Transparent Mode)"
time.sleep(2)
print ">> HC-12 Setup OK!"

# Usage
ser.write("[rf_msg] Dragonboard (Gateway) to Device")
GP.cleanup()
time.sleep(2)

# Infinite Loop for Data Receiver (Gateway)
while True:
    dataReceived = ser.read(10) # Read 10 bytes
    if dataReceived == "xxxxxxxx":
        print ">> Shutting down RX service..."
        break
    print dataReceived
    
    #Constant message to device (test)    
    #time.sleep(1)
    #ser.write(str(datetime.now()) + '\n')
    #time.sleep(1)

ser.close()


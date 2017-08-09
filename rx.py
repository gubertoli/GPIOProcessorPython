#
# Linker Sprite Mezzannine Board - RF (HC-12) x UART
#
# Required python-serial:
#   pip install pyserial
#   easy_install -U pyserial
#


import serial, time
from datetime import datetime
from GPIOProcessor import GPIOProcessor

ser = serial.Serial('/dev/tty96B0',baudrate=9600)

def config():
    # HC-12 Configuration
    # Using UART port from Low Speed Connector (PINs 5 and 7)
    
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
    time.sleep(1)
    SETPin.high()               # Enter Transparent Mode
    print ">> SET PIN ---> HIGH (Transparent Mode)"
    time.sleep(2)
    print ">> HC-12 Setup OK!"

    # Usage
    ser.write("[rf_msg] Dragonboard (Gateway) to Device")
    GP.cleanup()
    time.sleep(2)

def main():
    config()
    # Infinite Loop for Data Receiver (Gateway)
    while True:
        line = ser.readline()
        print line
    
    ser.close()

if __name__ == "__main__":
    main()


from network import Sigfox
import socket
import time
import machine
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

#DS18B20 data line connected to pin P23
ow = OneWire(Pin('P23', mode=Pin.OUT))
temp = DS18X20(ow)

#init Sigfox for EU 868 Mhz band. Must be initialized first.
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

#Creating a Socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

#Sets the socket to block, meaning we wait for the socket operation to complete.
s.setblocking(True)

#Here we set the socket to be uplink only, so in this example we can only send data.
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

#Send a string trough Sigfox. Strings will automatically be converted into hexadecimal trough Sigfox.
while True:
    temp.read_temp_async()
    time.sleep(1)
    temp.start_convertion()
    time.sleep(1)
    tempString = str(temp.read_temp_async()) + " C."
    print(tempString)
    time.sleep(1)
    s.send(tempString)
    time.sleep(60)

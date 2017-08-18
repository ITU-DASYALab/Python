from network import Sigfox
import socket
import time
import machine

#init Sigfox for EU 868 Mhz band. Must be initialized first.
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

#Create a Sigfox Socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

#Sets the socket to block, meaning we wait for the socket operation to complete.
s.setblocking(True)

#Here we set the socket to be uplink only, so in this example we can only send data.
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

#Send a basic string trough Sigfox. Can be seen in the Sigfox backend
s.send("Hello World")

#Send a basic string trough Sigfox. Can be seen in the Sigfox backend
s.send("Hello World")

#Send a basic byte array trough Sigfox. Can be seen in the sigfox backend
s.send(bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

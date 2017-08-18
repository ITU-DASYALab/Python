from network import Sigfox
import binascii

# initalise Sigfox for RCZ1 (RCZ1 is the EU standard. You may need a different RCZ Region)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# Print Sigfox Device ID
print(binascii.hexlify(sigfox.id()))

# Print Sigfox PAC number
print(binascii.hexlify(sigfox.pac()))

# Print Sigfox radio MAC adress
print(binascii.hexlify(sigfox.mac()))

import time
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

# onewire libary can be found here: https://github.com/micropython/micropython/blob/master/drivers/onewire/onewire.py

# Code for making the DS18B20 run on Arduino can be found here: https://create.arduino.cc/projecthub/TheGadgetBoy/ds18b20-digital-temperature-sensor-and-arduino-9cc806

#DS18B20 data line connected to pin P23
ow = OneWire(Pin('P23', mode=Pin.OUT))
temp = DS18X20(ow)

#Basic loop that prints the value read on the DS18B20 sensor
while True:
    print(temp.read_temp_async())
    time.sleep(1)
    temp.start_convertion()
    time.sleep(1)

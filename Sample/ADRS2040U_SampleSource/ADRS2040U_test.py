#=======================================================
# i2c_test.py : ADRS2040U PICO HAT Test Program
#       2022.09.08  V0.0    New Create
#       2022.10.26  V1.0    for ADRS2040U Ver 1.0    
#=======================================================
import time
import smbus

unit = 0.005035477      # int to degree
bus = smbus.SMBus(1)

while True:
    # LED on
    bus.write_word_data(0x41, 0x20, 1)
    # read temp
    temp = bus.read_word_data(0x41, 0x10) * unit
    print('Temp:', temp)
    # LED off
    bus.write_word_data(0x41, 0x20, 0)
    time.sleep(1.0)
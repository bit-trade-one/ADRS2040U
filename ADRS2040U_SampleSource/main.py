#=======================================================
# lm35_slave.py : ADRS2040U PICO HAT Test Program
#       2022.09.14  V0.0    New Create
#       2022.10.26  V1.0    for ADRS2040U Ver 1.0    
#=======================================================
import utime
import time
from machine import mem32,Pin
from i2cSlave import i2c_slave

unit = 0.005035477
# led pin config
led = Pin(25, Pin.OUT)  # GP25を出力モードに設定
# led off
led.value(0)
# ADC on
lm35 = machine.ADC(0)   # ADC0にLM35を接続

# i2c as slave
rp_i2c = i2c_slave(0, sda = 0, scl = 1, slaveAddress = 0x41)
rp_i2c.putWord(0)        # dummy write for bus lock
while True:
    cmd = 0
    val = 0
    temp = lm35.read_u16()  # read ADC
    if rp_i2c.any():
        cmd = rp_i2c.get()
        if cmd == 0x10 :
            while not rp_i2c.anyRead():
                pass
            rp_i2c.putWord(temp)
            #print('Temp:', temp * unit)
        elif cmd == 0x20 :
            val = rp_i2c.getWord()
            #print('val :', val)
            if val == 0 :
                led.value(0)
            elif val == 1 :
                led.value(1)          



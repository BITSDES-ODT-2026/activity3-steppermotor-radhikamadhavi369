from machine import Pin
import time

in1 = Pin(13,Pin.OUT)
in2 = Pin(14,Pin.OUT)
in3 = Pin(15,Pin.OUT)
in4 = Pin(19,Pin.OUT)

while True:
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    time.sleep(0.005)
    
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(0)
    time.sleep(0.005)
    
    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    time.sleep(0.005)
    
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    time.sleep(0.005)


Steppermotor rotating clock wise and aniticlockwise ;

from machine import Pin
import time

in1 = Pin(13,Pin.OUT)
in2 = Pin(14,Pin.OUT)
in3 = Pin(15,Pin.OUT)
in4 = Pin(19,Pin.OUT)

numbers = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
nb = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[0,0,0,0]]

while True:
    for k in range(500):
        for i in numbers:
            in.value(i[0])
            in.value(i[1])
            in.value(i[2])
            in.value(i[3])
            time.sleep_ms(5)
        
    for x in range(500):
        for s in r_di:
            in.value(s[0])
            in.value(s[1])
            in.value(s[2])
            in.value(s[3])
            time.sleep_ms(5)
            
    

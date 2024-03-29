from machine import Pin
from NetConnect import *
import time


net1 = NetTools("MianNMN_Net", "12345678")

def detect(net_object):
    pin_in = Pin(14, Pin.IN, Pin.PULL_DOWN)
    pin_led = Pin(2, Pin.OUT)
    while True:
        if not pin_in.value():
            pin_led.value(1)
            net_object.SendTCP("192.168.43.252", 8080, "shortage")
            time.sleep(1)
        else:
            pin_led.value(0)
            print("not shortage")
            time.sleep(5)
        
        
if __name__ == "__main__":
    net1 = NetTools("MianNMN_Net", "12345678")
    detect(net1)
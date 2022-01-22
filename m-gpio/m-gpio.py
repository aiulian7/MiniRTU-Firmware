from machine import Pin, PWM, SPI
import time

PINS = {1: 4, 2: 5, 3: 15, 4: 16, 5: 17, 6: 18, 7: 19, 8: 20,
        9: 21, 10: 22, 11: 23, 12: 24}
RELAY = {1: 10, 2: 7, 3: 6}

MOSFET = {1: 12, 2: 13, 3: 14, 4: 25}

class mgpio:
    def __init__(self):
        for index in range(3):
            R =  Pin(RELAY.get(index+1, None), Pin.OUT)  
            R.value(0)
        for index in range(4):
            P =  Pin(MOSFET.get(index+1, None), Pin.OUT)  
            P.value(0)
        pass
    
    def PIN(self, pin):
        return PINS.get(pin, None)
    
    def Relay(self, relay_no, relay_state):
        R =  Pin(RELAY.get(relay_no, None), Pin.OUT)  
        R.value(relay_state)
        
    def Mosfet(self, mosfet_no, mosfet_state, pwm_duty = 0, pwm_freq = 50):
        if pwm_duty:
            P_pwm = PWM(Pin(MOSFET.get(mosfet_no, None)))
            P_pwm.freq(pwm_freq)
            if mosfet_state:
                
                P_pwm.duty_u16(int(map(pwm_duty, 0, 100, 0, 65025)))
            else:
                pass
        else:
            P =  Pin(MOSFET.get(mosfet_no, None), Pin.OUT)  
            P.value(mosfet_state)
        pass

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
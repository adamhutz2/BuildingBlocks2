import time
from adafruit_crickit import crickit

ss = crickit.seesaw

BUTTON_1 = crickit.SIGNAL1

ss.pin_mode(BUTTON_1, ss.INPUT_PULLUP)

while True:
    if not ss.digital_read(BUTTON_1):
        print("Button 1 pressed")
        
    else:
        print("Button 1 NOT pressed")
        
    time.sleep(1)
        

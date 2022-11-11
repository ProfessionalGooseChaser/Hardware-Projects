import osascript as oa
from pynput.mouse import Controller
#import the rotary library
#from machine import Pin

def setVolume(val):
    oa.osascript("set volume output volume " + str(val))

knob = Controller()

def Scrolling(val):
    knob.scroll(0, val)

setVolume(50)

Scrolling(50)
















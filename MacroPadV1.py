#packages I need
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time
#from rotary_irq_rp2 import RotaryIRQ
#from machine import Pin

#setting up the connection to my speakers
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))



#Set's volume
def setVolume(val):
    scale = -10
    vrange = volume.GetVolumeRange()
    if (val * scale < vrange[1]):
        val = 0
    elif (val * scale > vrange[0]):
        val = 10
    volume.setMasterVolumeLevel(scale * val, None)
    
setVolume(5)

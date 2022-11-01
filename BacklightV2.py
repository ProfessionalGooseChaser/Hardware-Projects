from PIL import ImageGrab
import time
import multiprocessing as mp
import threading
from queue import Queue

start = time.time()

class light():
    def __init__(self, x, y, Xr, Yr):
        self.x = x
        self.y = y
        self.Xr = Xr
        self.Yr = Yr
        self.rgb = ()

    def average2(self):
        sqr = ImageGrab.grab(bbox = (self.x, self.y, self.x + self.Xr, self.y + self.Yr))
        px = sqr.load()
        totalRGB = (0, 0, 0)
        for x in range(self.Xr):
            for y in range(self.Yr):
                totalRGB = tuple(map(sum, zip(px[x,y], totalRGB))) 
        RGB = tuple(ti/(self.Xr * self.Yr) for ti in totalRGB)
        self.rgb = RGB

    #def most common (so much more complex)

    def __str__(self):
        return str(self.rgb)

class my_thread(threading.Thread):
    stop_event = threading.Event()
    queue = Queue()


class my_process(mp.Process):
    


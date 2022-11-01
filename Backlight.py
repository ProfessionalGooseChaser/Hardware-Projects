from PIL import ImageGrab
import time
from threading import *
from queue import Queue
import concurrent.futures

start = time.time()

SCREEN = (1440, 900)
_LIGHTS = []

def average2(minX, minY, rangeX, rangeY, LIGHTS):
    sqr = ImageGrab.grab(bbox = (minX, minY, minX + rangeX, minY + rangeY))
    px = sqr.load()
    totalRGB = (0, 0, 0)
    for x in range(rangeX):
        for y in range(rangeY):
            totalRGB = tuple(map(sum, zip(px[x,y], totalRGB))) 
    rgb = tuple(ti/(rangeX * rangeY) for ti in totalRGB)
    LIGHTS.append(rgb)

lights = []
for i in range(16): #90pixels for range 
    temp = (i*90, 0, 90, 25) #top row
    lights.append(temp)
    temp2 = (i*90, 1415, 90, 25) #bottom row
    lights.append(temp2)

for j in range(10):
    temp = (0, j*90, 25, 90) #Left side
    lights.append(temp)
    temp2 = (875, j*90, 25, 90)
    lights.append(temp2) #right side

start2 = time.time()


#Creates threads for each light, class functions suck so I did this and multithreaded it instead
threads = [Thread(target=average2, args=(n[0], n[1], n[2], n[3], _LIGHTS)) for n in lights]
[t1.start() for t1 in threads]

#just needed to see some time calues
end = time.time()
print(str(start2-start))
print(str(end-start2)) #takes regularly 10 seconds to boot

queue = Queue()
#10 iterations
count = 0
while(count < 10):
    count += 1
    start3 = time.time()
    #only runs the first time, and then stops
    for i in range(len(threads)):
        queue.put(i)
    if __name__ == '__main__':
        [t3.join() for t3 in threads]
    #send values to board
    print(time.time() - start3) # this time is always within .001 seconds, yeah but it's not doing it again
    _LIGHTS = []
    print(len(_LIGHTS))

   

#https://docs.python.org/3/library/asyncio-eventloop.html
#https://stackoverflow.com/questions/45609784/control-a-loop-in-a-thread-class-python


#1mil - 48.25s
#100k - 5.17s
#10k - 0.78s
#1k - 0.4s
#100 - 0.4s

#some notes, I'm not too worried about time rn. I do want to eventually use parallelt processing to update all of the lights at onces

#More notes, I optimized with multithreading.
#except it only works on the first one, it doesn't recalculate the data

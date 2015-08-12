from slidingwindow import SlidingWindow
import os,time
def generator():
    x = 0
    while x < 10:
        x += 1
        yield (x,)

def square(x):
	time.sleep(1)
	print x*x, os.getpid()

sl = SlidingWindow(size = 5, target=square, tasks = generator())
sl.start()
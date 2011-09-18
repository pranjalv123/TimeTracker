import time
import thread
import os

basedir = "/home/pranjal/usagedata/"

def get_filename(t):
    return basedir + time.strftime("%Y-%m-%d", t)
while True:
    inp = os.popen("xdotool getwindowfocus | xargs xprop _NET_WM_NAME -id")
    nm = inp.readline().split('"')[-2]
    tm = time.localtime()
    f = open(get_filename(tm), "a")
    tofday = time.strftime("%H:%M:%S", tm)
    f.write(tofday + " => " + nm + "\n")
    f.close()
    time.sleep(5)



import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


print("Item exists : " + str(path.exists("Webpage.txt")))

print("Item is a file : " + str(path.isfile("Webpage.txt")))

print("Item is a Directory  : " + str(path.isdir("Webpage.txt")))

print("Item path : " + str(path.realpath("Webpage.txt")))

print("Item path : " + str(path.split(path.realpath("Webpage.txt"))))

t = time.ctime(path.getmtime("Webpage.txt"))

print(t)

print(datetime.datetime.fromtimestamp(path.getmtime("Webpage.txt")))


td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("Webpage.txt"))

print("It has been " +str(td) + "Since the file was modified")

print("0r, "+str(td.total_seconds())+ "Seconds")

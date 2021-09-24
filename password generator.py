#!/usr/bin/env python3

#version - 1.0.0

import os
import sys
import random
import time

def color():

	(os.system("color 2"))

color()

print("version - 1.0.0.")

beginning = int(input("\n\n\nfrom what date should I generate a password - "))
end = int(input("\nfrom what date should I finish generating a password - "))

allfunction = str(random.randint(beginning, end))

time.sleep(1)

print("\n\n\n[+] | time - {0}  | PC - {1} | result - {2}   |.".format(str(time.asctime()), str(os.getlogin()), str(allfunction)))

(os.startfile("write down your passwords here.txt"))

time.sleep(1)

sys.exit()

# goodzero110
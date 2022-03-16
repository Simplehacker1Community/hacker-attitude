import os
import sys
import os 
from os import system
import time
system('clear')
system('apt update && clear && apt install espeak cmatrix python -y && clear')

for kt in range(20):
    system('espeak Wellcome to The hacking world')
    # normal
    system('cmatrix')
    time.sleep(5)
    #  Asynchronous scroll 
    system('espeak If your bad')
    system('cmatrix -a')
    time.sleep(5)
    # Japanese Character's 
    system('espeak I am Your dad')
    system('cmatrix -c')
    time.sleep(5)
    #  X Window Mode 
    system('espeak my attitude')
    system('cmatrix -x')
    time.sleep(5)
    # Change Color RED
    system('espeak My rules')
    system('cmatrix -C red')
    time.sleep(5)
    # Rainbow Mode 
    system('espeak your attitude')
    system('cmatrix -r')
    time.sleep(5)
    # Lambda Mode
    system('espeak my foot')
    system('cmatrix -m')
    time.sleep(5)
    # Bold characters on
    system('espeak your dad is back')
    system('cmatrix -B')
    time.sleep(3)
    system('clear')



system('rm robot.py')

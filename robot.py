##=========================================##
##=============PROJECT INFO================##
##=========================================##
##===Auther : SM02 Present=================##
##===Date   : 17/03/2022===================##
##===About  : attitude stutas on cmatrix===##
##===Version : 1.0 auto====================##
##=========================================##
##=============EMD INFO====================##
##=========================================##

import multiprocessing
import time
from os import system

# Your foo function
def foo(n):
    for i in range(10000 * n):
        system('cmatrix -r')
        time.sleep(1)

if __name__ == '__main__':
    # Update termux
    system('clear')
    system('apt update && clear && apt install espeak cmatrix python -y && clear')

    # Start foo as a process
    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    p.start()
    # Wait 10 seconds for foo
    time.sleep(2)
    # Terminate foo
    p.terminate()
    # Cleanup
    p.join()
    system('espeak Wellcome to The hacking world')
    # normal
    system('cmatrix')
    time.sleep(5)
    # Terminate cmatrix
    p.terminate()
    #  Asynchronous scroll 
    system('espeak If your bad')
    system('cmatrix -a')
    time.sleep(5)
    # Terminate cmatrix
    p.terminate()
    # Japanese Character's 
    system('espeak I am Your dad')
    system('cmatrix -c')
    time.sleep(5)
    # Terminate cmatrix
    p.terminate()
    #  X Window Mode 
    system('espeak my attitude')
    system('cmatrix -x')
    time.sleep(5)
    # Terminate cmatrix
    p.terminate()
    # Change Color RED
    system('espeak My rules')
    system('cmatrix -C red')
    time.sleep(5)
    # Terminate cmatrix
    p.terminate()
    # Rainbow Mode 
    system('espeak your attitude')
    system('cmatrix -r')
    time.sleep(5)
    # Terminate cmatrix
    p.terminate()
    # Lambda Mode
    system('espeak my foot')
    system('cmatrix -m')
    time.sleep(5)
    # Terminate cmatrix
    p.terminate()
    # Bold characters on
    system('espeak your dad is back')
    system('cmatrix -B')
    time.sleep(3)
    # Terminate cmatrix
    p.terminate()
    system('clear')
    
    
    
    

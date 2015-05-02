import sys
from canrecording import *
from time import *
from ctypes import *
libc = cdll.LoadLibrary('libc.so.6')
libcanopen = cdll.LoadLibrary('libcanopen.so')

sock = libcanopen.can_socket_open_timeout('vcan0', 0)
recording=canrecording('../../capture/can0-1423730484.pcap')
x=0
for timing,pkt in recording.Packets():

    if x % 1000 == 0:
        print x

    libc.write(sock,byref(pkt),c_int(16))

    x+=1

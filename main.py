import pcap,sys
from time import *
from ctypes import *
libc = cdll.LoadLibrary('libc.so.6')
libcanopen = cdll.LoadLibrary('libcanopen.so')

sock = libcanopen.can_socket_open_timeout('vcan0', 0)

inp=pcap.pcap("../capture/can0-1424041603.pcap")

x,prevTS,skew,toSleep,preSleep=0,0,0,0,0
for ts,pkt in inp:
    buf=(c_uint8*16)()
    for i in range(0,4): #Copy header (it's somehow backwards)
        buf[i]=ord(pkt[3-i])
    for i in range(4,len(pkt)):
        buf[i]=ord(pkt[i])

    if x % 1000 == 0:
        print x

    if prevTS > 0:
        toSleep=ts-prevTS
    prevTS=ts

    if skew > 0:
        toSleep-=skew

    if toSleep > 0:
        preSleep=time()
        sleep(toSleep)
        postSleep=time()
        skew=postSleep-preSleep-toSleep

    libc.write(sock,byref(buf),c_int(16))

    x+=1

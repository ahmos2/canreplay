import pcap,sys
from pycanopen import *
from ctypes import *

print 1
inp=pcap.pcap("../capture/can0-1424041603.pcap")
print 2,inp
outp=CANopen("vcan0")
print 3,outp
for ts,pkt in inp:
    print pkt,len(pkt)
    buf=bytearray(16)
    print len(buf)
    buf[0:len(pkt)]=pkt
    print len(buf)
    outp.write_can_frame(CANFrame.from_buffer_copy(buf))

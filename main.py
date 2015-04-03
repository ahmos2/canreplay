import pcap,sys
from pycanopen import *
from ctypes import *

inp=pcap.pcap("../capture/can0-1424041603.pcap")
outp=CANopen("vcan0")
for ts,pkt in inp:
    buf=bytearray(16)
    buf[0:len(pkt)]=pkt
    outp.write_can_frame(CANFrame.from_buffer_copy(buf))

from pcap import *
from ctypes import *
from time import *

class canrecording(object):
    def __init__(self, fileName):
        self.pcap = pcap(fileName)
    def Packets(self):
        timing,pkt = self.pcap.next() #Get first packet
        timingDifference = time() - timing
        while(True):
            while(time() > timing + timingDifference):
                buf=(c_uint8*16)()
                for i in range(0,4): #Copy header (it's somehow backwards)
                    buf[i]=ord(pkt[3-i])
                for i in range(4,len(pkt)):
                    buf[i]=ord(pkt[i])
                yield (timing, buf)
                timing,pkt = self.pcap.next()
        sleep(0)

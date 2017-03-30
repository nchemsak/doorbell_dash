## repurpose: ac:63:be:de:a0:63 (NSS)
## multivitamins: f0:27:2d:4a:96:a9 (NSS)
## wilsonjones: 84:d6:d0:da:43:b4 (no label - NSS Guest)
## MilkBaby: 0c:47:c9:ac:35:56 (NSS Guest)
## Pets: 68:54:fd:38:e1:8c (home)
## The Laundress: 44:65:0d:10:21:a9 (home, but flakey)

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from take_pic import pic
from rasp_camera import vid
from time import sleep
from send_text import SMStext
import datetime

timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
file = "".join(["doorbell pressed!! Time: ", timestamp])

def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        #if pkt[ARP].psrc:

            # Photo Trigger
        if pkt[ARP].hwsrc == '0c:47:c9:ac:35:56':
            print(file)
            pic()
            #vid()

            # Video Trigger
        elif pkt[ARP].hwsrc == '84:d6:d0:da:43:b4':
            print("doorbell 2 pressed")
            vid()

if __name__ == "__main__":
    sniff(prn=arp_display, filter="arp", store=0, count=0)
    #sniff(prn=arp_display, filter="arp", store=0, count=0, stop_filter=stopfilter)

    

##https://phaethon.github.io/scapy/getting-started/
   
##sniff([count=0,] [prn=None,] [store=1,] [offline=None,] [lfilter=None,] + 
##      L2ListenSocket args) -> list of packets
##
##  count: number of packets to capture. 0 means infinity
##  store: wether to store sniffed packets or discard them
##    prn: function to apply to each packet. If something is returned,
##         it is displayed. Ex:
##         ex: prn = lambda x: x.summary()
##lfilter: python function applied to each packet to determine
##         if further action may be done
##         ex: lfilter = lambda x: x.haslayer(Padding)
##offline: pcap file to read packets from, instead of sniffing them
##timeout: stop sniffing after a given time (default: None)
##L2socket: use the provided L2socket
##opened_socket: provide an object ready to use .recv() on
##stop_filter: python function applied to each packet to determine
##             if we have to stop the capture after this packet
##             ex: stop_filter = lambda x: x.haslayer(TCP)


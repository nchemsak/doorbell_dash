# repurpose: ac:63:be:de:a0:63 (NSS)
# multivitamins: f0:27:2d:4a:96:a9 (NSS)
# wilsonjones: 84:d6:d0:da:43:b4
# MilkBaby: 0c:47:c9:ac:35:56 (not registered)
# Pets: 68:54:fd:38:e1:8c
# The Laundress: 44:65:0d:10:21:a9 (home, but flakey)

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from take_pic import pic
from rasp_camera import vid
from send_text import SMStext

def arp_display(pkt):

    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc:

            # Photo Trigger
            if pkt[ARP].hwsrc == 'ac:63:be:de:a0:63':
                print("doorbell pressed")
                pic()
                SMStext()

            # Video Trigger
            elif pkt[ARP].hwsrc == 'f0:27:2d:4a:96:a9':
                 print("doorbell 2 pressed")
                 vid()


if __name__ == "__main__":
    sniff(prn=arp_display, filter="arp", store=0, count=0)



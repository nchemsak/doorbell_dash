# run script as SUDO
# To discover dash MAC address, push button down for 3 seconds until it pulses blue, connect your computer wifi to "Amazon ConfigureMe", in a web browser, go to: http://192.168.0.1/

# repurpose: ac:63:be:de:a0:63 (NSS)
# multivitamins: f0:27:2d:4a:96:a9 (NSS)
# wilsonjones: 84:d6:d0:da:43:b4
# MilkBaby: 0c:47:c9:ac:35:56 (not registered)
# Pets: 68:54:fd:38:e1:8c
# The Laundress: 44:65:0d:10:21:a9 (home, but not working)

# look at TWILIO for push notifications

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import cv2
from take_pic import pic
import datetime

# print("hello1")
def arp_display(pkt):
    # print("hello2")
    # url_pc = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=APA91bHfGjW5DLr7PiK3506crvxnvZLobVDxnibjYdHI1TxlB-FXNSzcJ-mixOasBpFObCSJ8QFAKGWwZ6OH9q0AiorlbIwTMJ5rslYtga4Yqr3qDz_2mzSzKCwi6R-bLdMviVGH-yvi&message=doorbell pressed'
    # url_mobile = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=APA91bHfGjW5DLr7PiK3506crvxnvZLobVDxnibjYdHI1TxlB-FXNSzcJ-mixOasBpFObCSJ8QFAKGWwZ6OH9q0AiorlbIwTMJ5rslYtga4Yqr3qDz_2mzSzKCwi6R-bLdMviVGH-yvi&message=doorbell pressed'

    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc:
            if pkt[ARP].hwsrc == 'ac:63:be:de:a0:63':
                print("doorbell pressed")
                pic()

if __name__ == "__main__":
    sniff(prn=arp_display, filter="arp", store=0, count=0)



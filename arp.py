# run script as SUDO
# repurpose: ac:63:be:de:a0:63
# multivitamins: f0:27:2d:4a:96:a9
# wilsonjONes: 84:d6:d0:da:43:b4
# MilkBaby: 0c:47:c9:ac:35:56

# look at TWILIO for push notifications

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from take_pic import pic

def arp_display(pkt):
    # url_pc = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=APA91bHfGjW5DLr7PiK3506crvxnvZLobVDxnibjYdHI1TxlB-FXNSzcJ-mixOasBpFObCSJ8QFAKGWwZ6OH9q0AiorlbIwTMJ5rslYtga4Yqr3qDz_2mzSzKCwi6R-bLdMviVGH-yvi&message=doorbell pressed'
    # url_mobile = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=APA91bHfGjW5DLr7PiK3506crvxnvZLobVDxnibjYdHI1TxlB-FXNSzcJ-mixOasBpFObCSJ8QFAKGWwZ6OH9q0AiorlbIwTMJ5rslYtga4Yqr3qDz_2mzSzKCwi6R-bLdMviVGH-yvi&message=doorbell pressed'

    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc:
            if pkt[ARP].hwsrc == 'f0:27:2d:4a:96:a9':
                print("doorbell pressed")
                take_pic()

if __name__ == "__main__":
    sniff(prn=arp_display, filter="arp", store=0, count=0)



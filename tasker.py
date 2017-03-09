"""********************
Doorbell script redone for python3
must run pip3 install scapy-python3

********************"""

from scapy.all import *
import urllib.request

def arp_display(pkt):

    url_pc = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=APA91bHfGjW5DLr7PiK3506crvxnvZLobVDxnibjYdHI1TxlB-FXNSzcJ-mixOasBpFObCSJ8QFAKGWwZ6OH9q0AiorlbIwTMJ5rslYtga4Yqr3qDz_2mzSzKCwi6R-bLdMviVGH-yvi'
    url_mobile = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=APA91bHfGjW5DLr7PiK3506crvxnvZLobVDxnibjYdHI1TxlB-FXNSzcJ-mixOasBpFObCSJ8QFAKGWwZ6OH9q0AiorlbIwTMJ5rslYtga4Yqr3qDz_2mzSzKCwi6R-bLdMviVGH-yvi'
    if pkt.haslayer(ARP):
        if pkt[ARP].op == 1:
            # if pkt[ARP].psrc == '0.0.0.0':
            if pkt[ARP].hwsrc == 'f0:27:2d:4a:96:a9': #Your button MAC
                button = 'BUTTON 1'
                #putting URL together before sent
            if 'button' in locals():
                messagePc = url_pc + button
                messageMobile = url_mobile + button
                #sending message to pc/mobile
                response = urllib.request.urlopen(messagePc).read()
                response = urllib.request.urlopen(messageMobile).read()

                #print ("Call from: " + button) #unhash for testing
            #print (pkt[ARP].hwsrc) #unhash for finding MAC of your button
print (sniff(prn=arp_display, filter="arp", store=0, count=0))

from scapy.all import *
import urllib.request

def arp_display(pkt):

    # url_pc = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=ENTER_YOUR_KEY_HERE&message='
    # url_mobile = 'http://autoremotejoaomgcd.appspot.com/sendmessage?key=ENTER_YOUR_KEY_HERE&message='

    if pkt[ARP].op == 1:
    #this line is no longer here (if pkt[ARP].psrc == '0.0.0.0':)
        if pkt[ARP].hwsrc == '34:13:e8:3c:3e:3f': #Your button MAC
            button = 'You clicked the Wilson Jones Dash Button'
        # elif pkt[ARP].hwsrc == 'AMAZON DASH MAC': #Other button
        #     button = 'Button2'
        # elif pkt[ARP].hwsrc == 'AMAZON DASH MAC': #Other button
        #     button = 'Button3'

#putting URL together before sent (checks if button variable is present)
        if 'button' in locals():
            messagePc = url_pc + button
            messageMobile = url_mobile + button
#ending message to pc/mobile
            response = urllib.request.urlopen(messagePc).read()
            response = urllib.request.urlopen(messageMobile).read()
#print ("Call from: " + button) #unhash for testing
#print (pkt[ARP].hwsrc) #unhash for finding MAC of your button
print (sniff(prn=arp_display, filter="arp", store=0, count=0))

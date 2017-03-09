from scapy.all import *

def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc: # ARP Probe - Address Resolution Protocol - ARP is used for mapping a network address (e.g. an IPv4 address) to a physical address like an Ethernet address (also named a MAC address).
            print ("ARP: " + pkt[ARP].hwsrc)

sniff(prn=arp_display, filter="arp", store=0, count=0)


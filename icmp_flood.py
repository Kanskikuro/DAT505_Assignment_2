from scapy.all import *

ip_hdr = IP(dst="192.168.50.210")

packet = ip_hdr / ICMP() 

#while true
for i in range(10):
        send(fragment(packet))

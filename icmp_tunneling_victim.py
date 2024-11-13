# victim
from scapy.all import sniff, IP, ICMP

def extract_covert_data(packet):
    if packet.haslayer(ICMP):
        icmp_payload = bytes(packet[ICMP].payload)
        if icmp_payload:
            print("Received covert data:", icmp_payload.decode(errors='ignore'))

if __name__ == "__main__":
    print("Sniffing for ICMP packets...")
    sniff(filter="icmp", prn=extract_covert_data, store=0)

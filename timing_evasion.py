from scapy.all import IP, TCP, sr1
import time
import random

def syn_scan(target_ip, target_ports):
    open_ports = []

    for port in target_ports:
        # Create a TCP packet with the SYN flag set (SYN scan)
        tcp_packet = IP(dst=target_ip) / TCP(sport=4444, dport=port, flags="S")

        # Send the packet and capture the response
        response = sr1(tcp_packet, timeout=1, verbose=0)

        # Check if the response has a TCP layer and the SYN-ACK flags are set (indicating an open port)
        if response and response.haslayer(TCP):
            if response[TCP].flags == 18:  # 18 = SYN-ACK (flags value indicating an open port)
                open_ports.append(port)
                print(f"Found open port: {port}")
    time.sleep(random.uniform(1,5))

    return open_ports

if __name__ == "__main__":
    target_ip = "192.168.50.210"  # Set the target IP address
    target_ports = range(1, 65535)  # Specify the range of ports to scan

    # Perform the SYN scan
    open_ports = syn_scan(target_ip, target_ports)

    # Print the open ports found
    if open_ports:
        print(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {target_ip}")

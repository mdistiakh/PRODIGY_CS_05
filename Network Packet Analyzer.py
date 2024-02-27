import socket
import struct

soc = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

soc.bind(("en0", 0))

while True:
    packet = soc.recvfrom(65536)

    e_head = packet[0][0:14]
    ip_head = packet[0][14:34]
    tcp_head = packet[0][34:54]

    print("Ethernet header:")
    print(e_head)

    print("IP header:")
    print(ip_head)

    print("TCP header:")
    print(tcp_head)

    payload = packet[0][54:]

    print("Payload:")
    print(payload)
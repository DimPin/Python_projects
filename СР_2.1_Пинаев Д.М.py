# import socket
# def scan_ports(target_host, port_list):
#     print(f"Scanning ports on {target_host}...")
#     for port in port_list:
#         try:
#             sock = socket.socket (socket. AF_INET, socket.SOCK_STREAM)
#             result = sock.connect_ex((target_host, port))
#             if result == 0:
#                 print(f"Port {port}: Open")
#             else:
#                 print(f"Port {port}: Closed")
#             sock.close()
#         except socket.error:
#             print(f"Could not connect to {target_host}:{port}")
#         print(f"Port scanning finished.")
# target_host = "192.168.1.1"
# port_list = [80, 443, 22, 3389]
# scan_ports(target_host, port_list)

import socket, sys
from struct import *

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error as msg:
    print(f"Socket could not be created. Error Code : + {str(msg[0])} + Message + {msg[1]}")
    sys.exit()
    
while True:
    packet = s.recvfrom(65565)
    packet = packet[0]
    ip_header = packet[0:20]
    iph = unpack('!BBHHHBBH4s4s', ip_header)
    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    iph_length = ihl * 4
    ttl = iph[5]
    protocol = iph[6]
    s_addr = socket.inet_ntoa(iph[8]);
    d_addr = socket.inet_ntoa(iph[9]);
    print
    'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(
    protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
    tcp_header = packet[iph_length:iph_length + 20]
    tcph = unpack('!HHLLBBHHH', tcp_header)
    source_port = tcph[0]
    dest_port = tcph[1]
    sequence = tcph[2]
    acknowledgement = tcph[3]
    doff_reserved = tcph[4]
    tcph_length = doff_reserved >> 4
    print (f" Source Port : + {str(source_port)} + Dest Port : + {str(dest_port)} + Sequence Number : + {str(sequence)} + Acknowledgement : + {str(acknowledgement)} + TCP header length : + {str(tcph_length)}")
    h_size = iph_length + tcph_length * 4
    data_size = len(packet) - h_size
    data = packet[h_size:]
    print(f"Data : + {data}:")
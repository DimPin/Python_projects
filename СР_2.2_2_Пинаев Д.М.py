import scapy.all as scapy

MAX_SIZE=60000

def detector(pkt):
    if scapy.UDP in pkt:
        if pkt[scapy.UDP].len > MAX_SIZE:
            print("Внимание! Подозрительно большой размер пакета ({}): src_IP={}, dst_IP={}, src_PORT={}, dst_PORT={}".format(pkt[scapy.UDP].len, pkt[scapy.IP].src, pkt[scapy.IP].dst, pkt[scapy.UDP].sport, pkt[scapy.UDP].dport))

def main():
    scapy.sniff(prn=detector, store=0)
if __name__ == "__main__":
    main()


import socket

UDP_IP = "192.168.0.1"
UDP_PORT = 1337
MESSAGE = b"L"*61000

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
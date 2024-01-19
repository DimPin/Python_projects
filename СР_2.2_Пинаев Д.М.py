import scapy.all as scapy
import time
MAX_COUNT_AVR=10
start_time = time.time()
counter = 0
def detector(pkt):
    global start_time
    global counter
    if scapy.UDP in pkt and pkt.dport == 1337:
        counter += 1
        timespan = time.time() - start_time
        if counter/timespan > MAX_COUNT_AVR:
            print("Внимание! Подозрительно большое число пакетов: {}шт за {}сек ({}шт/сек)".format(counter, timespan, counter/timespan))

def main():
    scapy.sniff(prn=detector, store=0)
if __name__ == "__main__":
    main()

import socket

UDP_IP = "192.168.0.1"
UDP_PORT = 1337
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
count = 0

while count < 1000:
    count+=1
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
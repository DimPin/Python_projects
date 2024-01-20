import scapy.all as scapy

def process_arp(pkt):
    if scapy.ARP in pkt:
        print("Получен пакет ARP: src_IP={}, dst_IP={}, src_MAC={}, dsc_MAC={}".format(pkt.psrc, pkt.pdst, pkt.hwsrc, pkt.hwdst))

def main():
    scapy.sniff(filter="arp", prn=process_arp)

if __name__ == "__main__":
    main()
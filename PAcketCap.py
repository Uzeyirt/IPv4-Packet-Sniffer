from scapy.all import *;

import datetime;

class Packet_Catcher(Thread) :
    def __init__(self,ip_address_assigned,Int_Name):
        Thread.__init__(self);

        self.running = True;

        self.Ip = ip_address_assigned ;

        self.Interface_Name = Int_Name ;

    def packet_callback(self,packet):

        if '(IPv4)' in packet.layers()[0].mysummary(packet) :

            if (packet[IP].dst == self.Ip):
                if packet.haslayer(ICMP):
                    print('source IP: ' + packet[IP].src + ' dest IP: ' +  packet[IP].dst + ' TTL: ' + str(packet[IP].ttl) + ' IP ID: ' + str(packet[IP].id)  + ' type: ' + str(packet[ICMP].type) + ' code: ' + str(packet[ICMP].code) );
                if packet.haslayer(UDP) :
                    print('source IP: ' + packet[IP].src + ' dest IP: ' + packet[IP].dst + ' TTL: ' + str(packet[IP].ttl) + ' IP ID: ' + str(packet[IP].id) + ' src port: ' + str(packet[UDP].sport) + ' dst port: ' + str(packet[UDP].dport));
                if packet.haslayer(TCP) :
                    print('source IP: ' + packet[IP].src + ' dest IP: ' + packet[IP].dst + ' TTL: ' + str(packet[IP].ttl) + ' IP ID: ' + str(packet[IP].id) + ' src port: ' + str(packet[TCP].sport) + ' dst port: ' +str(packet[TCP].dport));
    def _TheSniff(self,e):

        print( 'port sniffer added for port : ' + str(self.Interface_Name));
        sniff(iface = self.Interface_Name,prn = self.packet_callback,stop_filter = lambda p: e.is_set());

    def stop(self):

        self.running = False;




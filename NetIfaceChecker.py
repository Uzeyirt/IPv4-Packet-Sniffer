
import netifaces ;
from threading import Thread;
import time;
from PacketCapCreator import Packet_catcher_creator;

class IP_Finder(Thread) :



    def __init__(self,delay_second,p_c_c):
        Thread.__init__(self)
        self.IP_Address_List = [];
        self.Active_Interface_List = [];
        self.running = True ;
        self.delay = delay_second ;
        self.PCC = p_c_c ;
    def run(self):

        while self.running:
            self.IP_Address_List = [];
            self.Active_Interface_List = [];
            Interface_List_in_local_machine = netifaces.interfaces();

            for interfacee in Interface_List_in_local_machine:

                addrs = netifaces.ifaddresses(interfacee);

                if 2 in addrs:  # 2 is key which exist in operational interfaces

                    addresses = addrs[netifaces.AF_INET];

                    ip_adress_of_operational_interface = addresses[0]['addr'];

                    if (ip_adress_of_operational_interface.split('.')[0] != '127'):

                        if (interfacee is not self.Active_Interface_List):

                            self.IP_Address_List.append(ip_adress_of_operational_interface);

                            self.Active_Interface_List.append(interfacee);

            self.PCC.Interface_List = self.Active_Interface_List ;

            self.PCC.IP_Addresses_List = self.IP_Address_List ;

            time.sleep(self.delay);
    def stop(self):
        self.running = False
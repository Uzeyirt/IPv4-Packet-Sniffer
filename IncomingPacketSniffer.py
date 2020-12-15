#!/usr/bin/env python
import os

from NetIfaceChecker import IP_Finder;
from PacketCapCreator import Packet_catcher_creator;
import time;
global Packet_Counter ;

timeout=input('A timeout value is needed for check operation of network interfaces. Please enter a timeout(seconds):');
print(''
      'Sniffing is starting... After sniffing is started, press enter to stop sniffing'
      '');
time.sleep(5);
Pcc = Packet_catcher_creator(int(timeout));

ip_finder = IP_Finder(int(timeout),Pcc);

ip_finder.start();

Pcc.start();

empty=input("");

ip_finder.stop();

Pcc.stop();

print("Sniffing has been stopped..");


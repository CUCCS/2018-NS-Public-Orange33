import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "192.168.100.4"
src_port = RandShort()
dst_port=53
dst_timeout=10

udp_scan_resp = sr1(IP(dst=dst_ip)/UDP(dport=dst_port),timeout=dst_timeout)
if (str(type(udp_scan_resp))=="<type 'NoneType'>"):
    print("Port %d is Open|Filtered"%dst_port)
elif (udp_scan_resp.haslayer(UDP)):
    print("Port %d is Open"%dst_port)
elif(udp_scan_resp.haslayer(ICMP)):
    if(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code)==3):
        print("Port %d is Closed"%dst_port)
    elif(int(udp_scan_resp.getlayer(ICMP).type)==3 and int(udp_scan_resp.getlayer(ICMP).code) in [1,2,9,10,13]):
        print("Port %d is Filtered"%dst_port)

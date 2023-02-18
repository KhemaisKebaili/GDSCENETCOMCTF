from scapy.all import *
pqs=rdpcap("./iseeempee.pcap")
x=""
for pq in pqs[::2]:
    x+=chr(pq["ICMP"].id)
print(x)

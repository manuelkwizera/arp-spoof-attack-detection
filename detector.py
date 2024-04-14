from scapy.all import Ether, ARP, srp, sniff, conf

"""
we will send the arp request to the target machine of which we want to obtain its 
orginal mac address. hence this will make an ARP request and retrive the real mac address
"""

def get_mac(ip):
    """
    Returns the MAC address of `ip`, if it is unable to find it
    for some reason, throws `IndexError`
    """

    """
    we create an ARP request arp_request using ARP Function 
    and retrieves the real MAC address
    """

    p = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
    result = srp(p, timeout=3, verbose=False)[0]
    return result[0][1].hwsrc
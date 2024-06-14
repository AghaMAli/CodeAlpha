from scapy.all import get_if_list, sniff
import chardet
import pprint

# Step 1: List all available network interfaces
interfaces = get_if_list()
print("Available interfaces:", interfaces)

# Replace 'eth0' with the correct interface name from the printed list
interface = 'Wi-Fi'  # e.g., 'Ethernet', 'Wi-Fi', etc.
timeout = 10
promisc = True

try:
    # Step 2: Sniff packets using the correct interface name
    sniffer = sniff(iface=interface, timeout=timeout, promisc=promisc)
    for packet in sniffer:
        # Use show2() instead of show() to handle non-ASCII characters
        packet.show2()
        # Alternatively, use pprint() for a more readable output
        # pprint.pprint(packet)
except OSError as e:
    print(f"Error opening adapter: {e}")
except Exception as e:
    print(f"Error: {e}")
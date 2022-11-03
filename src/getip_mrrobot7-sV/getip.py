from tkinter import Tk
from netifaces import interfaces, ifaddresses, AF_INET
import argparse

# 
# NAME
#           getip - get IPv4 from network interface and copy to clipboard.
#
# SYNOPSIS
#           getip [-v] -i [interface]
# 
# AUTHOR
#           John Abraham, <pdv.dev07@outlook.com>

def get_ip_address(iname):
    for ifaceName in interfaces():
        if (iname == ifaceName):
            addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]  
            return ' '.join(addresses)
    return None

def copy_to_clipboard(ip):
    # copy IPv4 to the clipboard using tkinter (Python 3)
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(ip)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

def main():
    try:
        parser = argparse.ArgumentParser(prog ="getip", usage="%(prog)s -i [interface]", description="get IPv4 from network interface and copy to clipboard.")
        parser.add_argument('-i','--interface', help="the name of the network interface.", type=str, required=False)
        parser.add_argument('-v', help="more verbose output", action='store_true', required=False)
        args = parser.parse_args()
        
        # set default network interface and otherwise from argument.
        interface = 'tun0'
        if (args.interface):
            interface = args.interface 

        ip = get_ip_address(interface)
        if ip != None:
            if args.v:
                print(f"IP [{ip}] for network interface [{interface}] copied to clipboard.")
            copy_to_clipboard(ip)
        else:
            print("No IPv4 address found for that network interface.")        

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
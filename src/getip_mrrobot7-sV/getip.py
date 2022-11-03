import subprocess
from tkinter import Tk
import re
import argparse

# 
# NAME
#           getip - get IPv4 from network interface and copy to clipboard.
#
# SYNOPSIS
#           getip [-v] -i [interface]
# 
# 
# Author: mrrobot7-sV
# version: 1.0
# System requirements: Python 3, ???
# 

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
    
        # set up command to get IP address
        cmd = ["ip", "-br", "a", "show", interface]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = proc.communicate()

        # IPv4 address pattern
        ip = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', output.decode('ascii')).group(0)
        if args.v:
            print(f"IP [{ip}] for network interface [{interface}] copied to clipboard.")

        # copy IPv4 to the clipboard using tkinter (Python 3)
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(ip)
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
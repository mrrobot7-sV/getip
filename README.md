# getip
Get IPv4 from network interface and copy to clipboard.
# Installation

Download [getip.py](src/getip_mrrobot7-sV/getip.py)

# How to use
```
python3 ./getip [-v] -i [interface]
python3 ./getip.py -v -i tun0 
python3 ./getip.py -i tun0
python3 ./getip.py -h
```

# Example
```
$ python3 ./getip.py -v -i tun0
IP [100.19.14.45] for network interface [tun0] copied to clipboard.
```

## Tip

Create an alias:
```
alias getip='<path-to-python-script> -i tun0'
```

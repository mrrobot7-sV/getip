# getip
Get IPv4 from network interface and copy to clipboard.

# How to use
```
python3 ./getip.py -i [interface] -v
python3 ./getip.py -i tun0 -v
python3 ./getip.py -i tun0
python3 ./getip.py -h
```

# Example
```
$ python3 ./getip.py -i tun0 -v
IP [10.10.14.27] for network interface [tun0] copied to clipboard.
```

## Tip

Create an alias:
```
alias getip='<path-to-python-script> -i tun0'
```

import os
import colorama
import pyfiglet as pf
from colorama import Fore, Back, Style

print(Fore.BLUE+Style.BRIGHT+Style.BRIGHT+pf.figlet_format("white00 P-scanner\n"))
print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"Created by SANTHOSH.S\n")
print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"[CORE OF NMAP]\n")

i = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"choose your option portscan or To get web ip [Enter p for portscan / for web ip w ] (ex:p/w) : ")


# global variable



def scansv (ip_addr, scan_type):
    os.system(f"nmap -{scan_type} {ip_addr} -T 3")
    print(Fore.GREEN+Style.BRIGHT+"\nScan finished")


def scanO(ip_addr, scan_type):
    os.system(f"nmap -{scan_type} {ip_addr} -T 3")
    print(Fore.GREEN+Style.BRIGHT+"\n Scan finished")


def scanA(ip_addr, scan_type):
    os.system(f"nmap -{scan_type} {ip_addr} -T 3")
    print(Fore.GREEN+Style.BRIGHT+"\n Scan finished")


def scanall (ip_addr, scan_type):
    os.system(f"nmap -sV -O {ip_addr} -T 3")
    print(Fore.GREEN+Style.BRIGHT+"\n Scan finished")


def ip_scan(input):
    os.system(f"traceroute {input}")


if i == "p":
    ip_addr = input(Fore.YELLOW + Style.BRIGHT + Style.BRIGHT + "Enter your target ip address: ")
    scan_type = input(Fore.LIGHTGREEN_EX + Style.BRIGHT + """\nEnter your scan type 
    1.sV = version scan
    2.O = os detection
    3.A = Enable OS detection, version detection, script scanning, and traceroute
    4.To select all type of scan = H
    EXAMPLE : sV , O , A , H : """)

    if scan_type == "sV":
        scansv(ip_addr, scan_type)

    if scan_type == "O":
        scanO(ip_addr, scan_type)

    if scan_type == "A":
        scanA(ip_addr, scan_type)

    if scan_type == "H":
        scanall(ip_addr, scan_type)

if i == "w":
    input = input("Enter your target website domain to get ip address ex:[google.com] : ")
    ip_scan(input)


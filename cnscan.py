import nmap
import threading
import time
import os

# ANSI color codes for coloring the text
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'
GREEN = '\x1b[43m'
RED = '\033[91m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
BRIGHT_YELLOW = '\033[93;1m'
BRIGHT_CYAN = '\033[96;1m'
BRIGHT_GREEN = '\x1b[92;1m'
BRIGHT_RED = '\033[91;1m'

LINE1_COLOR = '\033[94m'     # Blue
LINE2_COLOR = '\033[96m'     # Light Blue
LINE3_COLOR = '\033[97m'     # Lighter Blue
LINE4_COLOR = '\033[97m'     # White
# Global flag to indicate scan status
is_scanning = False

# Function to display the scanning animation
def display_scan_animation():
    global is_scanning
    is_scanning = True
    scan_indicator = ['|', '/', '-', '\\']
    i = 0
    while is_scanning:
        print(f"\rScan in Progress {scan_indicator[i % len(scan_indicator)]}", end="")
        time.sleep(0.5)
        i += 1

# Scan the local network
def scan_network(ip_range):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_range, arguments='-sn')
    return nm

# Main function
def main():
      # Banner
    print(f"{LINE1_COLOR}   ___ _ __  ___  ___ __ _ _ __  {RESET}")
    print(f"{LINE2_COLOR}  / __| '_ \\/ __|/ __/ _` | '_ \\ {RESET}")
    print(f"{LINE2_COLOR} | (__| | | \\__ \\ (_| (_| | | | |{RESET}")
    print(f"{LINE4_COLOR}  \\___|_| |_|___/\\___\\__,_|_| |_|{RESET}\n")
    # print(f"{WHITE}\n--------------------------------------\n Made with <3 Kitten Technologies{RESET}\n--------------------------------------\n")
    # Prompt for IP range
    ip_range = input(f"{CYAN}Enter the IP range to scan (e.g., '192.168.0.0/24'): {RESET}")
    # os.system('clear')  # Clear the screen
    print(f"\n{CYAN}Scanning | {ip_range}{RESET}")

    # Start the scan animation in a separate thread
    animation_thread = threading.Thread(target=display_scan_animation)
    animation_thread.start()

    # Perform the network scan
    global is_scanning
    nm = scan_network(ip_range)
    is_scanning = False

    # Wait for the animation to finish
    animation_thread.join()

    print(f"  {GREEN}Complete!{RESET}\n")
    print(f"{CYAN}IP Address\t\tHostname{RESET}")
    for host in nm.all_hosts():
        hostname = nm[host].hostname()
        print(f"{host}\t\t{YELLOW}{hostname}{RESET}")

    print(f"")

if __name__ == "__main__":
    main()

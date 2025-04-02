#!/usr/bin/env python3

# VOIDBAG Terminal Tool
# Created by Streaky x Voidbro

import sys
import os
from modules import beginner
from modules import amateur
from modules import pro

# Terminal Colors
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
RED = "\033[91m"

# Banner

def show_banner():
    print(f"{MAGENTA}" + r"""
 _    ______  ________  ____  ___   ______
| |  / / __ \/  _/ __ \/ __ )/   | / ____/
| | / / / / // // / / / __  / /| |/ / __
| |/ / /_/ // // /_/ / /_/ / ___ / /_/ /
|___/\____/___/_____/_____/_/  |_|\____/

   Terminal Hustle Engine – Build. Learn. Earn.
         Created by Streaky x Voidbro
""" + f"{RESET}")

# === TOOLS MENU ===
def show_tools():
    print(f"\n{CYAN}Choose Tools by Skill Level:{RESET}")
    print(f"{YELLOW}[1]{RESET} Beginner Tools")
    print(f"{YELLOW}[2]{RESET} Amateur Tools")
    print(f"{YELLOW}[3]{RESET} Pro Tools")
    print(f"{YELLOW}[B]{RESET} Back to main\n")

    choice = input(f"{BOLD}Pick a tool level (1/2/3/B): {RESET}")

    if choice == "1":
        print(f"\n{GREEN}Beginner Tools:{RESET}")
        print("- tunnelr.py (Python) — Expose localhost via Ngrok/Serveo")
        print(f"{CYAN}Usage:{RESET} python3 tools/tunnelr.py")

    elif choice == "2":
        print(f"\n{GREEN}Amateur Tools:{RESET}")
        print("- recon.go (Go) — Fast subdomain scanner")
        print(f"{CYAN}Usage:{RESET} go run tools/recon.go <domain> <wordlist.txt>")

    elif choice == "3":
        print(f"\n{GREEN}Pro Tools:{RESET}")
        print("- rustscan.rs (Rust) — Custom TCP scanner")
        print(f"{CYAN}Usage:{RESET} rustc tools/rustscan.rs -o rustscan && ./rustscan <ip>")

    elif choice.upper() == "B":
        return
    else:
        print(f"{RED}Invalid option. Returning to main.{RESET}")

# === MAIN MENU ===
def main():
    show_banner()
    print(f"{CYAN}Choose your skill level or module:{RESET}")
    print(f"{YELLOW}[1]{RESET} Beginner")
    print(f"{YELLOW}[2]{RESET} Amateur")
    print(f"{YELLOW}[3]{RESET} Pro")
    print(f"{YELLOW}[T]{RESET} Tools by Level\n")

    choice = input(f"{BOLD}Enter your choice: {RESET}")

    if choice == "1":
        beginner.run()
    elif choice == "2":
        amateur.run()
    elif choice == "3":
        pro.run()
    elif choice.upper() == "T":
        show_tools()
    else:
        print(f"{RED}Invalid choice. Please enter 1, 2, 3 or T.{RESET}")

if __name__ == "__main__":
    main()

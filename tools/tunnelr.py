#!/usr/bin/env python3

# tunnelr.py - Beginner tool to expose localhost via Serveo or Ngrok
import os

def run():
    print("\n[+] Tunnelr: Expose Localhost Easily")
    print("[1] Serveo (No install needed)")
    print("[2] Ngrok (Requires installed)")
    print("[B] Back\n")

    choice = input("Choose tunnel method: ").strip().lower()

    if choice == "1":
        port = input("Enter local port (e.g. 5500): ")
        print(f"\nLaunching Serveo tunnel on port {port}...")
        os.system(f"ssh -R 80:localhost:{port} serveo.net")
    elif choice == "2":
        port = input("Enter local port (e.g. 3000): ")
        print(f"\nLaunching Ngrok tunnel on port {port}...")
        os.system(f"ngrok http {port}")
    elif choice == "b":
        return
    else:
        print("Invalid option. Try again.")

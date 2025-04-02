# amateur.py - VOIDBAG Amateur Module

# Terminal Colors
RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"

# The run() function is called from voidbag.py when user chooses Amateur path
def run():
    print(f"\n{GREEN}[+] Welcome to the Amateur Arena{RESET}")
    print(f"{CYAN}You’ve leveled up. Now it's time to dig deeper, scan smarter, and strike harder.{RESET}\n")

    print(f"{YELLOW}==> Focused Learning Paths:{RESET}")
    print("- Understand IDOR (Insecure Direct Object Reference)")
    print("- Practice XSS (Cross-Site Scripting)")
    print("- Detect Open Redirects and abuse for auth bypass")
    print("- Learn about Local File Inclusion (LFI)")
    print("- Self-host phishing labs with Serveo/Ngrok")
    print("- Write basic Bash/Python automation tools")

    print(f"\n{YELLOW}==> Tools to Master:{RESET}")
    print("- Burp Suite Community Edition")
    print("- Nmap with custom scripts")
    print("- Sublist3r, Assetfinder, Amass")
    print("- Ngrok or Serveo for tunnel exposure")
    print("- Git, GitHub Pages, ShellCheck")

    print(f"\n{YELLOW}==> Projects to Try:{RESET}")
    print("- Create a test login page and tunnel it to public (safe lab only)")
    print("- Find and report a real IDOR on a low-security bug bounty target")
    print("- Write a script that grabs open directories via dorking")
    print("- Deploy a GitHub-hosted HTML phishing sim with warning banner")

    print(f"\n{YELLOW}==> Hustle Seed:{RESET}")
    print("Turn your Bash/Python scripts into real tools. Start a GitHub series called 'Amateur Arsenal'. Link them to a blog or YouTube for extra traffic.")

    print(f"\n{BOLD}You’re halfway through the Void. Keep pushing. Type 'voidbag' to return anytime.{RESET}\n")

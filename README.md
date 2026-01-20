
# Networking & Cybersecurity Tools

A collection of Python scripts designed to automate networking tasks and visualize core IT concepts. This repository is part of my journey as a BCA student specializing in Cybersecurity.

## 🛠 Project 1: Subnet & IP Analyzer

This tool helps visualize how IPv4 addresses are processed by hardware by converting decimal IPs into their binary equivalents and identifying Network/Host portions.

### 🚀 Features
- Converts standard IPv4 (Decimal) to Binary.
- Identifies Network vs. Host bit distribution based on CIDR notation.
- Helps students and IT professionals visualize subnetting logic.

### 📖 Learning Objectives
By building this, I mastered:
- The relationship between IP addresses and the 32-bit binary system.
- How Subnet Masks act as "filters" for network traffic.
- Python string manipulation and bitwise logic concepts.

The Example of Visual of IPv4 Subnet Structure
<img width="1000" height="200" alt="Figure_1" src="https://github.com/user-attachments/assets/8b47f9b8-bd42-44ba-929f-2262e480e99b" />

### 💻 How to Run
1. Ensure you have Python installed.
2. Run the script:
   ```bash
   python subnet_analyzer.py

## 🛠 Project Spotlight: Quick Connectivity Tester

The `quick_ping.py` script acts as a bridge between Python and your System Shell. It sends an **ICMP Echo Request** to a target and interprets the response.

### 💻 How It Works (The Logic)
1. **User Input:** You provide a target IP or Domain.
2. **Platform Check:** The script detects if you are on Windows or Linux to use the correct `ping` parameters.
3. **Hand-off:** Python sends the command to the OS Terminal.
4. **Analysis:** The script returns a success or failure verdict based on the terminal's exit code.

### 📊 Sample Output
```console
Enter the IP or Domain to ping: 8.8.8.8

--- Checking connectivity to 8.8.8.8 ---
Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=14ms TTL=117

-----------------------------------
RESULT: [✅] 8.8.8.8 is REACHABLE
-----------------------------------

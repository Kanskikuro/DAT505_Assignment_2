# DAT505 Assignment: Snort Evasion Techniques with Scapy

This repository contains Python scripts that utilize Scapy to test and demonstrate techniques for bypassing Snort intrusion detection systems. The assignment explores common evasion methods by crafting network packets in ways that can potentially evade detection by standard Snort rules. Each script showcases a unique evasion technique, providing insights into network security and detection limitations.

## Techniques Implemented

1. **Packet Fragmentation**  
   By fragmenting packets, the scripts break larger payloads into smaller fragments to avoid detection by signature-based IDS that may only inspect full packets.

2. **Timing-Based Evasion**  
   Introducing random or delayed packet intervals allows for evasion by mimicking legitimate traffic patterns, reducing the likelihood of triggering Snort's detection for rapid scans or floods.

3. **Obfuscating Attack Payloads**  
   Scripts embed potentially malicious payloads within legitimate-looking packet structures (e.g., HTTP requests) to avoid straightforward detection by Snort's content-based rules.

4. **ICMP Tunneling for Covert Communication**  
   Using ICMP packets as a covert channel, the code demonstrates how data can be hidden within network traffic that often goes unchecked by IDS systems.

## Contents

- **`fragmentation.py`** - Demonstrates packet fragmentation techniques.
- **`timing_evasion.py`** - Uses timing variations to evade detection.
- **`payload_obfuscation.py`** - Obfuscates payloads within legitimate packet structures.
- **`icmp_tunneling.py`** - Implements ICMP tunneling for covert data transmission.

## Usage

To run the scripts, ensure you have **Python** and **Scapy** installed:
```bash
pip install scapy
```

Each script requires root privileges to execute correctly. Run the scripts with:
```bash
sudo python <script_name>.py
```
##Disclaimer

This project is for educational purposes only and should only be used in a controlled environment. Unauthorized use of these techniques outside of approved environments may violate network policies or legal regulations

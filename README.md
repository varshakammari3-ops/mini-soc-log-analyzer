# Mini SOC Log Analyzer

A Python-based Security Operations Center (SOC) tool that analyzes authentication logs, detects repeated failed login attempts, identifies suspicious IP addresses, and generates a security report.

## Features

- Parses authentication log files
- Counts failed login attempts
- Groups failed attempts by IP address
- Detects possible brute-force activity
- Generates a security report
- Uses a configurable alert threshold

## Technologies

- Python 3
- File handling
- String parsing
- Dictionaries
- Basic security log analysis

## How It Works

The analyzer reads `sample_auth.log` and searches for `LOGIN_FAILED` events.

If an IP address generates 5 or more failed login attempts, the tool generates a security alert for possible brute-force activity.

## Example Detection

```text
[ALERT] Possible brute-force activity from 192.168.1.50 - 6 failed attempts

Output

The program generates:

security_report.txt

The report contains:

Total log entries
Total failed login attempts
Failed attempts by IP address
Security alerts
Security Note

The included log file contains fictional test data only. No real credentials or authentication logs are used.

Purpose

This project demonstrates basic SOC and security monitoring concepts, including log analysis, event detection, IP-based investigation, and automated alert generation.


Save it with **Ctrl + S**.

After saving, your project should have:

```text
mini-soc-log-analyzer/
├── log_analyzer.py
├── sample_auth.log
├── security_report.txt
└── README.md
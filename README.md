# 🛡️ Mini SOC Log Analyzer

A Python-based Security Operations Center (SOC) dashboard that analyzes authentication logs, detects repeated failed login attempts, identifies suspicious IP addresses, and generates security alerts.

The project includes a web-based dashboard built with Flask, HTML, CSS, and JavaScript for visualizing security events.

---

## 🚀 Features

- 📋 Authentication log analysis
- 🔐 Failed login detection
- 🌐 IP-based activity tracking
- 🚨 Brute-force activity detection
- 📊 Security statistics dashboard
- 🔎 Configurable detection threshold
- 🔄 Real-time log re-scan from the dashboard
- 📄 Automatic security report generation
- 💻 Responsive web interface
- 🔌 Flask API for security data

---

## 🏗️ Project Structure

```text
mini-soc-log-analyzer/
│
├── app.py
├── log_analyzer.py
├── sample_auth.log
├── security_report.txt
├── README.md
├── .gitignore
│
└── web/
    ├── index.html
    ├── style.css
    └── script.js

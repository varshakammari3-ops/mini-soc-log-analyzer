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

⚙️ Technologies Used
Python 3
Flask
HTML5
CSS3
JavaScript
File handling
Log parsing
Dictionary-based event tracking
REST-style API endpoint

**🔍 Detection Logic**

The analyzer searches authentication logs for failed login events.

Example:

LOGIN_FAILED user=admin ip=192.168.1.50

Failed attempts are grouped by IP address.

The current detection threshold is:

5 or more failed attempts

When an IP reaches the threshold, the dashboard generates a security alert indicating possible brute-force activity.

The alert is a detection rule based on repeated failed logins; it does not by itself prove that an attack occurred.

**🖥️ Dashboard**

The web dashboard displays:

Total log entries
Failed login attempts
Suspicious IP addresses
System monitoring status
Security alerts
Failed attempts by IP
Detection rules
Last scan time

The dashboard retrieves security data from the Flask backend through:

/api/security-data

**📦 Installation**

Clone the repository:

git clone https://github.com/varshakammari3-ops/mini-soc-log-analyzer.git

Enter the project directory:

cd mini-soc-log-analyzer

Install Flask:

pip install flask
▶️ Running the Project

Start the Flask application:

python app.py

The application will run locally.

Open the following address in your browser:

http://127.0.0.1:5000

**📊 Example Detection**

The sample log contains repeated failed login attempts from a test IP.

Example alert:

[ALERT] Possible brute-force activity from
192.168.1.50 - 6 failed attempts
📄 Security Report

The project can generate:

security_report.txt

The report contains:

Total log entries
Total failed login attempts
Failed attempts grouped by IP
Security alerts

**🧪 Sample Data**

The included:

sample_auth.log

contains fictional test data created specifically for this project.

No real authentication logs, passwords, or credentials are used.

**🔐 Security Considerations**

This project is intended for learning and defensive security monitoring.

The analyzer should be tested using fictional or authorized log data only.

Repeated failed login attempts can have legitimate causes, so alerts should be investigated using additional security information before treating them as confirmed attacks.

**🎯 Project Purpose**

This project demonstrates practical SOC concepts including:

Security log monitoring
Event detection
Failed authentication analysis
IP-based investigation
Brute-force detection logic
Security alert generation
Basic security dashboard development
**
📌 Future Improvements**

Possible future enhancements include:

Real-time log streaming
Login success/failure charts
Date and time filtering
Exportable reports
Multiple detection rules
Severity classification
Database integration
Authentication for dashboard access
Integration with additional security log sources

**👩‍💻 Author **

Varsha Kammari
Cybersecurity Project — Mini SOC Log Analyzer
Then **save `README.md`**.
After saving, VS Code terminal lo:

```bash
git add README.md

then:

git commit -m "Improve project documentation"

then:

git push

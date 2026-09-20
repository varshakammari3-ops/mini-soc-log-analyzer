from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="web", static_url_path="")

LOG_FILE = "sample_auth.log"
THRESHOLD = 5


def analyze_logs():
    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    failed_logins = 0
    failed_by_ip = {}

    for line in logs:
        if "LOGIN_FAILED" in line and "ip=" in line:
            failed_logins += 1

            ip = line.split("ip=")[1].strip()

            failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1

    suspicious_ips = {
        ip: count
        for ip, count in failed_by_ip.items()
        if count >= THRESHOLD
    }

    alerts = []

    for ip, count in suspicious_ips.items():
        alerts.append({
            "ip": ip,
            "failed_attempts": count,
            "severity": "High"
        })

    return {
        "total_logs": len(logs),
        "failed_logins": failed_logins,
        "suspicious_ips": len(suspicious_ips),
        "alerts": alerts,
        "failed_by_ip": failed_by_ip
    }


@app.route("/")
def home():
    return send_from_directory("web", "index.html")


@app.route("/api/security-data")
def security_data():
    return jsonify(analyze_logs())


if __name__ == "__main__":
    app.run(debug=True)
# Mini SOC Log Analyzer

log_file = "sample_auth.log"

# Read log file
with open(log_file, "r") as file:
    logs = file.readlines()

print("===== MINI SOC LOG ANALYZER =====")
print("Total log entries:", len(logs))

# Count failed login attempts
failed_logins = 0
failed_by_ip = {}

for line in logs:
    if "LOGIN_FAILED" in line:
        failed_logins += 1

        parts = line.split("ip=")
        ip = parts[1].strip()

        failed_by_ip[ip] = failed_by_ip.get(ip, 0) + 1

print("Failed login attempts:", failed_logins)
print("Failed attempts by IP:", failed_by_ip)

# Detect suspicious IPs
threshold = 5

print("\n===== SECURITY ALERTS =====")

for ip, count in failed_by_ip.items():
    if count >= threshold:
        print(
            f"[ALERT] Possible brute-force activity from "
            f"{ip} - {count} failed attempts"
        )

# Generate security report
with open("security_report.txt", "w") as report:
    report.write("===== MINI SOC SECURITY REPORT =====\n")
    report.write(f"Total log entries: {len(logs)}\n")
    report.write(f"Failed login attempts: {failed_logins}\n\n")

    report.write("Failed attempts by IP:\n")

    for ip, count in failed_by_ip.items():
        report.write(f"{ip}: {count}\n")

    report.write("\nSecurity Alerts:\n")

    for ip, count in failed_by_ip.items():
        if count >= threshold:
            report.write(
                f"ALERT: Possible brute-force activity from "
                f"{ip} ({count} failed attempts)\n"
            )

print("\nSecurity report saved as security_report.txt")
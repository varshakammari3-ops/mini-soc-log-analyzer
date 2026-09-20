// Mini SOC Dashboard

async function loadSecurityData() {
    try {
        const response = await fetch("/api/security-data");

        if (!response.ok) {
            throw new Error("Failed to fetch security data");
        }

        const data = await response.json();

        // Update statistics
        document.getElementById("totalLogs").textContent =
            data.total_logs;

        document.getElementById("failedLogins").textContent =
            data.failed_logins;

        document.getElementById("suspiciousIPs").textContent =
            data.suspicious_ips;

        // Update first security alert
        const alertCount = document.querySelector(".alert-count");

        if (data.alerts.length > 0) {
            const alert = data.alerts[0];

            document.getElementById("alertIP").textContent =
                "🌐 IP: " + alert.ip;

            document.getElementById("alertAttempts").textContent =
                "🔑 Failed Attempts: " + alert.failed_attempts;

            document.getElementById("alertSeverity").textContent =
                "⚠️ Severity: " + alert.severity;

            alertCount.textContent =
                `${data.alerts.length} Active Alert${data.alerts.length > 1 ? "s" : ""}`;
        } else {
            alertCount.textContent = "No Active Alerts";
        }

        // Update IP chart
        const chart = document.getElementById("ipChart");
        chart.innerHTML = "";

        const ipData = data.failed_by_ip;
        const counts = Object.values(ipData);

        if (counts.length === 0) {
            chart.innerHTML =
                '<p style="color:#9ca3af;">No failed login activity detected.</p>';
        } else {
            const maxAttempts = Math.max(...counts);

            for (const [ip, count] of Object.entries(ipData)) {

                const percentage =
                    (count / maxAttempts) * 100;

                let level = "low";

                if (count >= 5) {
                    level = "high";
                } else if (count >= 2) {
                    level = "medium";
                }

                const item = document.createElement("div");
                item.className = "bar-item";

                item.innerHTML = `
                    <div class="bar-label">
                        <span>${ip}</span>
                        <strong>${count}</strong>
                    </div>

                    <div class="bar">
                        <div
                            class="bar-fill ${level}"
                            style="width: ${percentage}%;">
                        </div>
                    </div>
                `;

                chart.appendChild(item);
            }
        }

        // Update last scan time
        const scanTime = new Date().toLocaleTimeString();

        document.getElementById("lastScan").textContent =
            "Last scan: " + scanTime;

        console.log("Security data loaded successfully.");

    } catch (error) {
        console.error("Error:", error);
    }
}


// Re-scan button
const scanButton = document.getElementById("scanButton");

if (scanButton) {
    scanButton.addEventListener("click", async function () {

        scanButton.disabled = true;
        scanButton.textContent = "⏳ Scanning...";

        await loadSecurityData();

        scanButton.disabled = false;
        scanButton.textContent = "🔄 Re-scan Logs";
    });
}


// Initial scan
loadSecurityData();
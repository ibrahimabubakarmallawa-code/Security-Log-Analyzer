
def detect_threats(parsed_logs):
    failed_attempts = {}

    for log in parsed_logs:

        if log is None:
            continue

        if log["event"] == "LOGIN_FAILED":
            ip = log["ip_address"]

            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    suspicious_ips = []

    for ip, count in failed_attempts.items():

        if count >= 3:
            suspicious_ips.append({
                "ip_address": ip,
                "failed_attempts": count,
                "status": "SUSPICIOUS"
            })

    return suspicious_ips

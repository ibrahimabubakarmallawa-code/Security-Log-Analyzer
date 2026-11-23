
def generate_report(suspicious_ips):

    print("\n========== SECURITY REPORT ==========")

    if not suspicious_ips:
        print("No suspicious activities detected.")

    else:
        print("Suspicious IP addresses detected:\n")

        for threat in suspicious_ips:
            print("IP Address:", threat["ip_address"])
            print("Failed Attempts:", threat["failed_attempts"])
            print("Status:", threat["status"])
            print("-----------------------------------")

    print("========== END OF REPORT ==========")

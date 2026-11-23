
def parse_log(log):
    parts = log.strip().split(",")

    if len(parts) == 4:
        return {
            "timestamp": parts[0],
            "ip_address": parts[1],
            "username": parts[2],
            "event": parts[3]
        }

    return None

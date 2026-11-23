
def read_logs(file_path):
    try:
        with open(file_path, "r") as file:
            logs = file.readlines()

        return logs

    except FileNotFoundError:
        print("Error: Log file not found.")
        return []

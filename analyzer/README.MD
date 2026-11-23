
# Security Log Analyzer

A Python-based cybersecurity tool that analyzes security log files, monitors login activities, and detects potentially suspicious login attempts.

## 1. Project Overview

The Security Log Analyzer is a practical cybersecurity project developed using Python.

It reads security log files, extracts relevant information, analyzes failed login attempts, and identifies IP addresses that generate repeated failed login attempts within a specified time window.

The project demonstrates how Python programming can be applied to basic cybersecurity monitoring and threat detection.

## 2. Features

- Reads security logs from files.
- Parses log records into structured data.
- Extracts timestamps, IP addresses, usernames, and login events.
- Counts failed login attempts by IP address.
- Detects suspicious login activities within a two-minute window.
- Generates security reports.
- Saves reports as text files.
- Handles missing log files.

## 3. Technologies Used

- Python 3
- Python datetime module
- File handling
- Dictionaries and lists
- Functions
- Modular programming

## 4. Project Structure

```text
Security-Log-Analyzer/
│
├── main.py
├── README.md
│
├── data/
│   └── security.log
│
├── analyzer/
│   ├── __init__.py
│   ├── log_reader.py
│   ├── log_parser.py
│   └── threat_detector.py
│
└── reports/
    ├── report_generator.py
    └── security_report.txt
```

## 5. How It Works

The application operates through four main stages:

1. **Log Reading:** Reads security records from the log file.
2. **Log Parsing:** Extracts information from each record.
3. **Threat Detection:** Analyzes login activities and identifies suspicious IP addresses.
4. **Report Generation:** Displays and saves the security analysis.

## 6. Sample Log Data

The application uses comma-separated log records.

```text
2026-11-17 08:10:15,192.168.1.10,ibrahim,LOGIN_SUCCESS
2026-11-17 08:12:20,192.168.1.15,ahmad,LOGIN_FAILED
2026-11-17 08:12:25,192.168.1.15,ahmad,LOGIN_FAILED
2026-11-17 08:12:30,192.168.1.15,ahmad,LOGIN_FAILED
```

Each record contains:

- Timestamp
- IP address
- Username
- Login event

## 7. Installation and Usage

### Requirements

- Python 3 installed.
- Visual Studio Code or another Python editor.

### Running the Application

1. Clone or download this repository.
2. Open the project folder in your terminal.
3. Run the following command:

```bash
python main.py
```

The application will read the security logs, analyze login activities, and generate a security report.

## 8. Threat Detection Rule

The current time-based detection rule identifies an IP address as suspicious when it makes at least three failed login attempts within a two-minute window.

This is a basic educational detection rule and does not independently prove that an attack has occurred.

## 9. Output

The application displays the security report in the terminal and saves it to:

```text
reports/security_report.txt
```

## 10. Future Improvements

- Export reports to CSV format.
- Introduce more advanced threat detection rules.
- Implement automated unit testing.
- Improve error handling and input validation.
- Develop a graphical user interface.
- Integrate additional security log sources.

## 11. Disclaimer

This project is developed for educational purposes to demonstrate Python programming, security log analysis, and basic cybersecurity threat detection.

## 12. Author

Developed as a practical Python and cybersecurity learning project.


from analyzer.log_reader import read_logs
from analyzer.log_parser import parse_log
from analyzer.threat_detector import detect_threats
from reports.report_generator import generate_report as write_report


class SecurityLogAnalyzer:
    """
    Main class responsible for coordinating security log analysis.
    """

    def __init__(self, file_path):
        """Initialize the analyzer with a log file path."""

        self.file_path = file_path
        self.logs = []
        self.parsed_logs = []
        self.suspicious_ips = []

    def load_logs(self):
        """Read security records from the log file."""

        self.logs = read_logs(self.file_path)
        return self.logs

    def parse_logs(self):
        """Convert raw log records into structured data."""

        self.parsed_logs = []

        for log in self.logs:
            parsed = parse_log(log)

            if parsed is not None:
                self.parsed_logs.append(parsed)

        return self.parsed_logs

    def analyze_logs(self):
        """Detect suspicious login activities."""

        self.suspicious_ips = detect_threats(self.parsed_logs)
        return self.suspicious_ips

    def generate_report(self):
        """Generate the security analysis report."""

        write_report(self.suspicious_ips)

    def run(self):
        """Execute the complete security analysis process."""

        self.load_logs()
        self.parse_logs()
        self.analyze_logs()
        self.generate_report()

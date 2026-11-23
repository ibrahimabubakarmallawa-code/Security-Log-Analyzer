
from analyzer.security_analyzer import SecurityLogAnalyzer


def main():
    """
    Start the Security Log Analyzer application.
    """

    # Create an object from the SecurityLogAnalyzer class
    analyzer = SecurityLogAnalyzer("data/security.log")

    # Display the object information
    print("Security Log Analyzer object created successfully!")

    # Execute the analysis using the object
    analyzer.run()


# Program entry point
if __name__ == "__main__":
    main()

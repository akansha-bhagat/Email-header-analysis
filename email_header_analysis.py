# Email Header Analysis Script
# Done By: Akansha Bhagat
# This script extracts key information such as From, To, Subject, Date from an email headers.

import re

def my_parse_email_header(header):
    # Simple regex to capture key components from the header
    email_data = {}

    # Extracting the "From" field
    from_match = re.search(r'From:\s*(.*)', header)
    if from_match:
        email_data['From'] = from_match.group(1)
    
    # Extracting the "To" field
    to_match = re.search(r'To:\s*(.*)', header)
    if to_match:
        email_data['To'] = to_match.group(1)

    # Extracting the "Subject" field
    subject_match = re.search(r'Subject:\s*(.*)', header)
    if subject_match:
        email_data['Subject'] = subject_match.group(1)
    
    # Extracting the "Date" field
    date_match = re.search(r'Date:\s*(.*)', header)
    if date_match:
        email_data['Date'] = date_match.group(1)

    return email_data

# Example email header to test the function
header_example = """
From: Akansha <akansha@example.com>
To: Support <support@example.com>
Subject: Application for an internship
Date: Tue, 23 Jan 2025 12:00:00 +0000
"""

# Parse and print the result
email_info = my_parse_email_header(header_example)
print("Parsed Email Header Information:")
for key, value in email_info.items():
    print(f"{key}: {value}")

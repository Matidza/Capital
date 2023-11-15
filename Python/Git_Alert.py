import requests
import smtplib
from email.mime.text import MIMEText

# Set your GitHub personal access token
ACCESS_TOKEN = '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'

# Set the repository details
OWNER = 'Matidza'
REPO = 'DLTA_CAP'

# Set the label or keyword for deadlines
DEADLINE_LABEL = 'deadline'

# GitHub API base URL
BASE_URL = 'https://api.github.com'

# Construct the headers with the access token
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

# Construct the API endpoint URL for issues
issues_url = f'{BASE_URL}/repos/{OWNER}/{REPO}/issues'

# Make the API request to fetch issues
response = requests.get(issues_url, headers=headers)
issues = response.json()

# Initialize the email server details
smtp_server = 'smtp.example.com'  # Replace with your SMTP server address
smtp_port = 587
smtp_username = 'Matidza46@gmail.com'
smtp_password = 'your_email_password'  # Replace with your email password

# Create the email connection
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Iterate through issues and check for deadlines
for issue in issues:
    if DEADLINE_LABEL in [label['name'] for label in issue['labels']]:
        subject = f"Upcoming Deadline for issue: {issue['title']}"
        message = f"The deadline for the issue '{issue['title']}' is approaching."

        # Create the email content
        email_content = MIMEText(message)
        email_content['From'] = smtp_username
        email_content['To'] = 'matidza46@gmail.ccom'  # Replace with the recipient's email address
        email_content['Subject'] = subject

        # Send the email
        server.sendmail(smtp_username, email_content['To'], email_content.as_string())

# Close the email connection
server.quit()

import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'supriyaprithiviraj@gmail.com'
email_password = 'Your_Password'
email_receiver = 'yntvni@gmail.com'

subject = 'My Python Prjects'
body = """
Automate Emails with Python
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
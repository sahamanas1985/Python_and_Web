import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
 
LOG_FILENAME = 'log.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# Define the SMTP server and port
smtp_server = "smtp.example.com"
port = 465  # For SSL
 
# Define sender's and receiver's email addresses
sender_email = "myemail@example.com"
receiver_email = "your.email@example.com"
 
# Define the email's subject and body
subject = "An email from Python"
body = "This is a test email sent from a Python script using SSL."
 
# Create a secure SSL context
context = ssl.create_default_context()
 
# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
 
# Send the email
try:
    
    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context) # Secure the connection with TLS
        server.login(sender_email, "your_password")
        
        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
    
    '''
    # Connect to the SMTP server
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        # Login to the server
        server.login(sender_email, "your_password")  # Replace with your password
 
        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
    '''
 
    print("Email sent successfully")
except Exception as e:
    logging.error(e, exc_info=True)
    print(f"Error sending email: {e}")
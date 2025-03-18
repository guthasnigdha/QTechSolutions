import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# User Input
sender_email = input("Enter your Gmail address: ")
password = getpass.getpass("Enter your email password: ")
recipient_email = input("Enter recipient email: ")
subject = input("Enter subject: ")
message_body = input("Enter message: ")

# Create MIME email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject
msg.attach(MIMEText(message_body, "plain"))

try:
    # Connect to SMTP Server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Secure connection
    server.login(sender_email, password)  # Login

    # Send email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    print("✅ Email sent successfully!")

except smtplib.SMTPAuthenticationError:
    print("❌ Authentication failed! Please check your email and password.")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    server.quit()  # Close server connection

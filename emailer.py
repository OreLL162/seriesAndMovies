import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config


def send_email(upcoming_items, choice, category):
    sender_email = config.SENDER_EMAIL
    receiver_email = config.RECEIVER_EMAIL
    password = config.EMAIL_PASSWORD

    email_content = f"We got some suggested {category.capitalize()} {choice.capitalize()} for you! :\n\n"
    for item in upcoming_items:
        email_content += f"Title: {item['title']}\nRelease Date: {item['release_date']}\nRating: {item['rating']}\n\n"

    # Create a multipart message and set headers
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"We got some {category.capitalize()} {choice.capitalize()} for you !"

    # Attach the body with the msg instance
    msg.attach(MIMEText(email_content, 'plain'))
    
    try:
        # Setup the server connection using SMTP
        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, password)  # Log in to your email account
            server.send_message(msg)  # Send the email
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
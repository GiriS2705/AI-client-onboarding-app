import smtplib
from email.mime.text import MIMEText

def send_email(to_email):
    msg = MIMEText("""
    Please upload:
    - Passport
    - Driving License

    Go to the app and upload your documents.
    """)

    msg['Subject'] = "Document Request"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login("your_email@gmail.com", "your_app_password")
            server.send_message(msg)
        return True
    except Exception as e:
        return str(e)
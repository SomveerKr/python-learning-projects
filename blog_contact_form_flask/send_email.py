import smtplib
from email.message import EmailMessage

class EmailSender:
    def __init__(self, sender_email, password, smtp_server="smtp.gmail.com", port=587):
        """
        Initializes the email sender with credentials and server details.
        """
        self.sender_email = sender_email
        self.password = password
        self.smtp_server = smtp_server
        self.port = port

    def send(self, receiver_email, subject, content):
        """
        Constructs and sends the email.
        """
        if not self.sender_email or not self.password:
            raise ValueError("Sender email and password must be provided.")

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        msg.set_content(content)

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as connection:
                connection.starttls()
                connection.login(self.sender_email, self.password)
                connection.send_message(msg)
                return True # Indicate success
        except smtplib.SMTPAuthenticationError:
            print("Error: Authentication failed. Check credentials.")
            return False
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
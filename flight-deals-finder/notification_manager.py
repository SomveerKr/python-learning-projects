from twilio.rest import Client
import os
from dotenv import load_dotenv
# This line loads the environment variables from the .env file
load_dotenv()
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):  
        message = self.client.messages.create(
        messaging_service_sid=os.getenv("TWILIO_MESSAGING_SERVICE_SID"),
        body=message_body,
        to=os.getenv("PHONE_NUMBER")
        )
        # Prints if successfully sent.
        print(message.status)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.status)
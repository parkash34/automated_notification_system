import os
import smtplib
import time
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from twilio.rest import Client

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    handlers=[
        logging.FileHandler("restaurant.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def send_email_smtp():
    return None


load_dotenv()

smtp_email = os.getenv("SMTP_EMAIL")
if not smtp_email:
    raise ValueError("SMTP EMAIL is missing in env")

smtp_password = os.getenv("SMTP_PASSWORD")
if not smtp_password:
    raise ValueError("SMTP PASSWORD is missing in env")

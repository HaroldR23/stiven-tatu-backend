from dotenv import load_dotenv
import os

load_dotenv()

COMPANY_EMAIL_RECIPIENT = os.environ.get("COMPANY_EMAIL_RECIPIENT", "default_recipient@example.com")
  
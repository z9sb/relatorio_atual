from __future__ import print_function
import base64
from email.mime.multipart import MIMEMultipart
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.base import MIMEBase
from pathlib import Path
from email import encoders

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']
creds = None
token_path = './src/secrets/token.json'
credentials_path = './src/secrets/credentials.json'

if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
# If there are no (valid) credentials available, let the user log in.

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(token_path, 'w') as token:
        token.write(creds.to_json())



def create_message_with_attachment(
    sender: str, recipient: str, subject: str, message_text: str, attachment_files: list
    ) -> dict:
    """
    Create a message for an email with an attachment.

    Args:
        sender (str): The email address of the sender.
        recipient (str): The email address of the recipient.
        subject (str): The subject of the email message.
        message_text (str): The text of the email message.
        attachment_files (list): A list of file paths to the attachments.

    Returns:
        A dictionary containing the message with the attachment.
    """
    message = MIMEMultipart()
    message['to'] = recipient
    message['from'] = sender
    message['subject'] = subject

    for file in attachment_files:
        with open(file, 'rb') as attachment:
            attachment_data = attachment.read()
            attachment_name = os.path.basename(file)

        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attachment_data)
        encoders.encode_base64(att)

        att.add_header('Content-Disposition', 'attachment', filename=attachment_name)
        message.attach(att)

    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    
def send_message(message):
    """
    Send an email message.

    Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.

    Returns:
        Sent Message.
    """
    try:
        user_id='me'
        service = build('gmail', 'v1', credentials=creds)
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print(message)
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(error)

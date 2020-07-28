import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import html2text

def parse_html(html_path):
  msg_html = open(html_path).read()
  msg_plain = html2text.html2text(msg_html)
  return msg_html, msg_plain

def create_message(sender, to, subject, msg_html, msg_plain):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    msg_html: The HTML of the message as a string.
    msg_plain: The plain text of the message as a string.  This is used as a fall back.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEMultipart('alternative')
  
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  
  body_mime = MIMEText(msg_plain, 'plain')
  message.attach(body_mime)
  
  html_mime = MIMEText(msg_html, 'html')
  message.attach(html_mime)
  
  print("Message \u2714", end = " ")
  return message

def create_draft(service, user_id, message_body):
  """Create and insert a draft email. Print the returned draft's message and id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message_body: The body of the email message, including headers.

  Returns:
    Draft object, including draft id and message meta data.
  """
  
  msg_raw = {'raw': base64.urlsafe_b64encode(message_body.as_string().encode("utf-8")).decode("utf-8")}
  message = {'message': msg_raw}
  
  try:
    draft = service.users().drafts().create(userId=user_id, body=message).execute()
    print("Draft \u2714", end = " ")

    return draft
    
  except Exception as e:
    print("An error occurred: {}".format(e))
    raise e

def main(learner_dict, service, subject, html_path):
  
  sender = "kcoapman@fishtownanalytics.com"
  to = learner_dict['email']
  msg_html, msg_plain = parse_html(html_path)

  message = create_message(sender, to, subject, msg_html, msg_plain)

  create_draft(service, "me", message)

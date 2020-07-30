from __future__ import print_function
from jinja2 import Environment, FileSystemLoader
import os
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import html2text

### Configure your mail merge here
compile_html = True
make_drafts = True
limit_num = 20
spreadsheet_id = '14QEhg0jHrUITL-ZNcbGrqinOOatDUPLdsmsy1hXY1oE'
spreadsheet_range = '2020-08-12 (London)!A1:P24'

### Future refactoring:
# Configure the following fields in this file RATHER than in the Google sheet:
# instructor_name, instructor_slack, channel_name, prework_due_date, intro_slide_link
# or even better, get these values form the _data folder in the learn.getdbt.com repo.

# Function for first time authentication and accessing the sheet
def getcredits():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly', 
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose']
    
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    print("We have the creds...")
    return creds

def sheets_service(creds):
    service = build('sheets', 'v4', credentials=creds)
    print("We built sheets service...")
    return service
    
def gmail_service(creds):
    service = build('gmail', 'v1', credentials=creds)
    print("We built gmail service...")
    return service
    
def get_sheet_values(service, spreadsheet_id, spreadsheet_range):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=spreadsheet_range).execute()
    values = result.get('values', [])
    print("We have the sheet values...")
    return values

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
  
  print("Message for {email} has been created.".format(email = to))
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
    print('Draft Created (Draft id: %s Draft message: %s)\n' % (draft['id'], draft['message']))
    return draft
    
  except Exception as e:
    print("An error occurred: {}".format(e))
    raise e

creds = getcredits()
sheets_service = sheets_service(creds)
learner_info_raw = get_sheet_values(sheets_service, spreadsheet_id, spreadsheet_range)

### Step 2: Use Jinja to create HTML files of the emails to be sent

if compile_html:
    gmail_service = gmail_service(creds)
    
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('email_template.html')

    headers = learner_info_raw[0]

    learners_as_list_of_lists = learner_info_raw[1:]
    learners_as_list_of_dict = []

    length = len(learners_as_list_of_lists[0])

    for learner in learners_as_list_of_lists:
        dict_temp = {}
        for i in range(length):
            dict_temp[headers[i]] = learner[i]
        learners_as_list_of_dict.append(dict_temp)
    
    limit_counter = 0
    
    for learner in learners_as_list_of_dict:
        if limit_counter == limit_num:
            break
        if learner['Contacted'] == 'Y':
            continue
        else:
            filename = os.path.join(root, 'html', learner['snowflake_user'] +  '.html')
            with open(filename, 'w') as fh:
                fh.write(template.render(learner))
            
            if make_drafts:
                ### Get the corresponding html file as a string
                html_path = "html/" + learner['snowflake_user'] + ".html"
                msg_html = open(html_path).read()
                msg_plain = html2text.html2text(msg_html)

                ### Get the corresponding learner data 
                sender = "kcoapman@fishtownanalytics.com"
                to = learner['email']
                subject = "Welcome to dbt Learn " + learner['first_name']+ "!"
                
                message = create_message(sender, to, subject, msg_html, msg_plain)
                create_draft(gmail_service, "me", message)
            
            limit_counter += 1
            
print("We have finished the job!")

from googleapiclient.discovery import build

def gmail_service(creds):
    service = build('gmail', 'v1', credentials=creds)
    print("We built gmail service...")
    return service

def main(creds):
    service = gmail_service(creds)
    return service
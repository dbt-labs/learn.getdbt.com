from googleapiclient.discovery import build

def sheets_service(creds):
    service = build('sheets', 'v4', credentials=creds)
    print("We built sheets service...")
    return service
    
def get_sheet_values(service, spreadsheet_id, spreadsheet_range):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range=spreadsheet_range).execute()
    values = result.get('values', [])
    print("We have the sheet values...")
    return values
    
def main(creds, spreadsheet_id, spreadsheet_range):
    service = sheets_service(creds)
    values = get_sheet_values(service, spreadsheet_id, spreadsheet_range)
    return values

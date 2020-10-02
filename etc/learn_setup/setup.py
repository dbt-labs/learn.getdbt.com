import auth_google
import read_sheets
import sf_open
import sf_query
import merge_html
import gmail_service
import write_draft
import yaml

# Change this file to choose the Learn that you want to send emails for
with open('./config/snowflake_creds.yml') as file:
    sf_creds = yaml.full_load(file)

snowflake_creds = sf_creds['snowflake']

with open('./config/beta_20201001.yml') as file:
    config = yaml.full_load(file)

html_template = config['html_template'] 
session_info = config['session']

# Get the credentials from .yml
spreadsheet_id = config['sheet']['spreadsheet_id']
spreadsheet_range = config['sheet']['spreadsheet_range']

# Authenticate with Google
creds = auth_google.main()

# Read the values from the Google Sheet
sheet_with_headers = read_sheets.main(creds, spreadsheet_id, spreadsheet_range)

# Open Snowflake Connection
cs, ctx = sf_open.main(snowflake_creds)

# Create Gmail Service
service = gmail_service.main(creds)

headers = sheet_with_headers[0]
learner_info = sheet_with_headers[1:]

print("Setting up each user: \n")

for learner in learner_info:
    learner_dict = dict(zip(headers, learner))    
    sf_username = learner_dict['sf_username']
    session_date = config['session']['date']

    if learner_dict['Contacted'] == 'Y':
        continue

    print("* {user}:".format(user = sf_username), end = " ")

    query1 = """
    create user {sf_username}
    password = 'ChangeMe123'
    must_change_password = true
    default_role = transformer
    default_warehouse = transforming
    comment = '{session_date}'
    days_to_expiry = 30;""".format(sf_username = sf_username, session_date = session_date)
    
    query2 = """
    grant role transformer to user {sf_username};""".format(sf_username = sf_username)

    # Create HTML file for email with Jinja
    joint_dict = {**learner_dict, **session_info}
    file_path = merge_html.main(joint_dict, html_template)
    
    # Create the email as a draft in Gmail
    subject = "Welcome to dbt Learn " + learner_dict['first_name'] + "!"
    write_draft.main(learner_dict, service, subject, file_path)

    # Submit Query
    sf_query.main(ctx, cs, query1)
    sf_query.main(ctx, cs, query2)

    print("DONE\n")

# Close the Snowflake Connection
cs.close()
ctx.close()
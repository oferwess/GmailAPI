from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# Define the scope for Gmail API
# SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
SCOPES = ['https://mail.google.com/']

def main():
    # Initialize the OAuth 2.0 flow with your credentials JSON file

    flow = InstalledAppFlow.from_client_secrets_file('D:\GitHub\Gmail API\provengo9-credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    
    # Build the Gmail API service
    service = build('gmail', 'v1', credentials=credentials)

    # List all messages in the Inbox
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    
    if not messages:
        print('No messages found.')
        return

    # Delete each message
    for message in messages:
        service.users().messages().delete(userId='me', id=message['id']).execute()
        print(f"Deleted message with ID: {message['id']}")

if __name__ == '__main__':
    main()

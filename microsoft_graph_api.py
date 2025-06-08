from msal import PublicClientApplication
from datetime import datetime, timedelta
import requests

CLIENT_ID_m = '57c05860-dceb-4348-a353-ffee143c23b6'
TENANT_ID_m = '2dded424-4409-4eea-abae-c0f93b9ccbb6'
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID_m}"
SCOPES = ["Mail.Read"]

app = PublicClientApplication(CLIENT_ID_m, authority=AUTHORITY)

# Interactive login
result = app.acquire_token_interactive(scopes=SCOPES)
access_token = result['access_token']


import requests

def get_unread_messages():
   
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json'
    }

    url = 'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messages?$filter=isRead eq false&$top=10&$orderby=receivedDateTime desc'


    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise error if the request failed
    messages = response.json().get('value', [])

    result = []
    for msg in messages:
        sender = msg['from']['emailAddress']['name']
        subject = msg['subject']
        print(f"From: {sender} - Subject: {subject}")
        result.append({'from': sender, 'subject': subject})

    return result



# Configuration
CLIENT_ID = 'cbe54967-5ec3-443b-9cbe-46a2e9295e68'
CLIENT_SECRET = 'HbD8Q~8FcCGY8Zr2_ZPf~BoWrl6RvPT5fPSEmbHW'
TENANT_ID = '2dded424-4409-4eea-abae-c0f93b9ccbb6'
USER_ID = 'me@domain.com'  # or 'me' for current user

# Get access token
def get_access_token():
    token_url = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'
    
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://graph.microsoft.com/.default'
    }
    
    token_response = requests.post(token_url, data=token_data)
    if token_response.status_code == 200:
        return token_response.json().get('access_token')
    else:
        raise Exception(f"Failed to get access token: {token_response.text}")

# Get calendar events
def get_calendar_events(start_date=None, end_date=None):
    access_token = get_access_token()
    
    # Set default date range if not provided
    if not start_date:
        start_date = datetime.utcnow().isoformat() + 'Z'
    if not end_date:
        end_date = (datetime.utcnow() + timedelta(days=30)).isoformat() + 'Z'
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Prefer': 'outlook.timezone="UTC"'
    }
    
    # URL for calendar events with date filter
    events_url = f'https://graph.microsoft.com/v1.0/users/{USER_ID}/calendar/events?' \
                f'$filter=start/dateTime ge \'{start_date}\' and end/dateTime le \'{end_date}\''
    
    response = requests.get(events_url, headers=headers)
    
    if response.status_code == 200:
        allevents=response.json().get('value', [])
        return allevents
    else:
        raise Exception(f"Failed to get calendar events: {response.text}")

# Main execution
if __name__ == '__main__':
    try:
        # Get events for the next 30 days
        events = get_calendar_events()
        
        print(f"Found {len(events)} events:")
        for event in events:
            print(f"\nSubject: {event.get('subject')}")
            print(f"Start: {event.get('start', {}).get('dateTime')}")
            print(f"End: {event.get('end', {}).get('dateTime')}")
            print(f"Organizer: {event.get('organizer', {}).get('emailAddress', {}).get('name')}")

    except Exception as e:
        print(f"Error: {str(e)}")



"""

Application (client) ID : cbe54967-5ec3-443b-9cbe-46a2e9295e68

Object ID : 5a012f28-94f0-45da-b55e-4bb3e335d1a5

Directory (tenant) ID : 2dded424-4409-4eea-abae-c0f93b9ccbb6
"""
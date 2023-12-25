# Gmail API integration with Python

## Purpose
This Python script is designed to interact with the Gmail API to perform activities on Gmail Account. <br />
The main function demonstrate delete all messages from the specified Gmail account's Inbox. <br />
You can change the main function for any action supported by Gmail API. <br />
It uses Google's Gmail API and requires user authentication. <br />
https://developers.google.com/gmail/api/reference/rest?hl=en <br />

## Configuration
Obtain Google API Credentials: <br />
1. Go to the Google Developers Console.
Create a new project or select an existing project.
2. Enable the Gmail API for your project.
Create credentials and download the client configuration file (JSON format).
3. Rename the downloaded file to your-account-credentials.json.
4. Place the credentials file in the same directory as the script.

Set Up Token File: <br />
During the first run, the GmailAPI-RefreshToken uses browser authentication to retive Refresh Token which will be use later on for future use (valid for 200 days). <br />
The script will generate a token file (token-your-account.json) to store authentication information. <br />
Ensure the script has write permissions in the working directory. <br />
<br />
## Prerequisites
Before running the script, ensure you have the following prerequisites installed:

- Python 3.x: [Download and Install Python](https://www.python.org/downloads/)
- pip: Python package installer. It is usually included with Python installations. If not, install it by following the [official instructions](https://pip.pypa.io/en/stable/installation/).

## Installation
Clone or download this repository to your local machine.

```bash
git clone https://github.com/oferwess/GmailAPI.git
cd GmailAPI
python GmailAPI-RefreshToken.py


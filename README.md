# Gmail API integration with Python

## Purpose
This Python script is designed to interact with the Gmail API to perform activities on Gmail Account
The main function demonstrate delete all messages from the specified Gmail account's Inbox. 
You can change the main function for any action supported by Gmail API
It uses Google's Gmail API and requires user authentication.
https://developers.google.com/gmail/api/reference/rest?hl=en

## Configuration
Obtain Google API Credentials:

Go to the Google Developers Console.
Create a new project or select an existing project.
Enable the Gmail API for your project.
Create credentials and download the client configuration file (JSON format).
Rename the downloaded file to your-account-credentials.json.
Place the credentials file in the same directory as the script.

Set Up Token File:
During the first run, the GmailAPI-RefreshToken uses browser authentication to retive Refresh Token which will be use later on for future use (valid for 200 days)
The script will generate a token file (token-your-account.json) to store authentication information.
Ensure the script has write permissions in the working directory.

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


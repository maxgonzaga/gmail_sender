# gmail_sender
Instructios for using this script.
Enable less secure apps on Gmail settings.
Install the required packages by running:
    pip install --requirement ./requirement.txt
Create a file called `.env` with the following content:
    EMAIL:your@email.com
    PASSWORD:your_password

## Usage:
    gmail.py (--to TO) [--subject SUBJECT] [--body BODY] [--file FILE]...
    gmail.py (-h | --help)
    gmail.py --version
    
## Options:
    --to TO
    --subject SUBJECT
    --file FILE
    --body BODY
    -h, --help  Show this screen
    --version  Show version
"""
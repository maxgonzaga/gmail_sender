"""gmail
Usage:
    gmail.py (--to TO) [--subject SUBJECT] [--body BODY] [--file FILE]...
    gmail.py (-h | --help)
    gmail.py --version
    
Options:
    --to TO
    --subject SUBJECT
    --file FILE
    --body BODY
    -h, --help  Show this screen
    --version  Show version
"""

# The code in https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/ was used as a blueprint for coding this script.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from docopt import docopt
import os
from dotenv import load_dotenv

load_dotenv('.env')

def main(args):
    message = MIMEMultipart()
    message['From'] = os.getenv('EMAIL')
    to = args['--to']
    message['To'] = to
    if (args['--subject']):
        message['Subject'] = args['--subject']
    if (args['--body']):
        body = args['--body']
        message.attach(MIMEText(body, 'plain'))
    if (args['--file']):
        for filename in args['--file']:
            attachment = open(filename, "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filename))
            message.attach(p)
    send_email(os.getenv('EMAIL'), to, message)
    print("Email sent")

def send_email(from_address, to_address, message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_address, os.getenv('PASSWORD'))
    text = message.as_string()
    s.sendmail(from_address, to_address, text)
    s.quit()

if __name__ == "__main__":
    args = docopt(__doc__, argv=None, help=True, version="0.1")
    main(args)

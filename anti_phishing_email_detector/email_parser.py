from email import message_from_string
# email_parser.py
import email
from email import policy
from email.parser import BytesParser, Parser

def parse_email_headers(raw_email):
    """
    Takes raw email text and returns a dict of headers
    """
    try:
        if isinstance(raw_email, str):
            msg = Parser(policy=policy.default).parsestr(raw_email)
        else:
            msg = BytesParser(policy=policy.default).parsebytes(raw_email)
        headers = {k: v for k, v in msg.items()}
        return headers
    except Exception as e:
        print(f"[ERROR] Parsing email headers failed: {e}")
        return {}

def parse_email(raw_email):
    msg = message_from_string(raw_email)

    headers = dict(msg.items())
    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += part.get_payload(decode=True).decode(errors="ignore")
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")

    return headers, body

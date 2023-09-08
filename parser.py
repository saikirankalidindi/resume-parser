from pdfminer.high_level import extract_text
import spacy
from spacy.matcher import Matcher
import re

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
patterns = [
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}],  # First name and Last name
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],  # First name, Middle name, and Last name
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]  # First name, Middle name, Middle name, and Last name
        # Add more patterns as needed
    ]
for pattern in patterns:
    matcher.add('NAME', patterns=[pattern])

text = extract_text('/home/saikiran/Downloads/resume.pdf')
doc = nlp(text)
matches = matcher(doc)
for match_id, start, end in matches:
    fullname = doc[start:end]
mobile_pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
email_match = re.search(email_pattern, text)
mobile_match = re.search(mobile_pattern, text)

if email_match:
    email = email_match.group()
if mobile_match:
    mobile = mobile_match.group()

contact_info = {
    'name': fullname,
    'mobile no': mobile,
    'email id': email
}

print(contact_info)







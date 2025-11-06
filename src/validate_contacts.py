"""
validate_contacts.py

Sample script to validate emails and phone numbers in a CSV and produce a cleaned CSV.

Usage:
    python src/validate_contacts.py path/to/contacts.csv
"""
import sys
import pandas as pd
import phonenumbers
import re
from pathlib import Path

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def validate_email(email):
    if pd.isna(email):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))

def validate_phone(number, default_region=None):
    if pd.isna(number):
        return False
    try:
        parsed = phonenumbers.parse(str(number), default_region)
        return phonenumbers.is_valid_number(parsed)
    except Exception:
        return False

def main(csv_path):
    df = pd.read_csv(csv_path)
    df['email_valid'] = df['email'].apply(validate_email)
    df['phone_valid'] = df['phone'].apply(lambda x: validate_phone(x, None))
    out_path = Path(csv_path).with_name("contacts_validated.csv")
    df.to_csv(out_path, index=False)
    print(f"Validated file written to: {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/validate_contacts.py path/to/contacts.csv")
    else:
        main(sys.argv[1])
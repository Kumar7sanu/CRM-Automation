"""
openai_extractor.py

Example of using OpenAI to extract website URLs or candidate sites from unstructured social text.
Requires OPENAI_API_KEY set in the environment.
"""
import os
import pandas as pd
import openai
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_urls_from_text(text):
    # Simple regex-based fallback extraction
    urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+|[^\s]+\.(com|co|uk|net|org))', text or "")
    if urls:
        return [u[0] for u in urls]
    return []

def openai_suggest(text):
    if not openai.api_key:
        return None
    prompt = f"Extract possible vendor website URLs from the following social text:\n\n{text}\n\nReturn a JSON array of URLs."
    resp = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
    return resp.choices[0].text.strip()

def main(csv_path):
    df = pd.read_csv(csv_path)
    df['extracted_urls'] = df['social_text'].apply(lambda x: extract_urls_from_text(x))
    out_path = "contacts_openai_extracted.csv"
    df.to_csv(out_path, index=False)
    print("OpenAI extraction (and regex fallback) written to:", out_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python src/openai_extractor.py path/to/contacts.csv")
    else:
        main(sys.argv[1])
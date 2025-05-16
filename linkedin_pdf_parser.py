import fitz  # PyMuPDF
import pandas as pd
import re
import os
import argparse

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def parse_linkedin_pdf(text):
    # Initialize fields
    profile = {
        "Name": "",
        "Headline": "",
        "Location": "",
        "About": "",
        "Experience": "",
        "Education": "",
        "Skills": "",
        "Licenses & Certifications": "",
        "Languages": "",
        "Projects": ""
    }

    # Split sections based on common LinkedIn headings
    sections = re.split(r'\n(?=[A-Z][a-z]+(?: & [A-Z][a-z]+)*\n)', text)

    # First lines are usually name, headline, and location
    lines = text.splitlines()
    if lines:
        profile["Name"] = lines[0].strip()
    if len(lines) > 1:
        profile["Headline"] = lines[1].strip()
    if len(lines) > 2:
        profile["Location"] = lines[2].strip()

    # Extract section content
    for section in sections:
        lower = section.lower()
        if "about" in lower:
            profile["About"] = section.strip()
        elif "experience" in lower:
            profile["Experience"] = section.strip()
        elif "education" in lower:
            profile["Education"] = section.strip()
        elif "skill" in lower:
            profile["Skills"] = section.strip()
        elif "certification" in lower:
            profile["Licenses & Certifications"] = section.strip()
        elif "language" in lower:
            profile["Languages"] = section.strip()
        elif "project" in lower:
            profile["Projects"] = section.strip()

    return profile

def main(pdf_path, output_csv):
    text = extract_text_from_pdf(pdf_path)
    profile_data = parse_linkedin_pdf(text)
    df = pd.DataFrame([profile_data])
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"Data extracted and saved to {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse LinkedIn PDF and export to CSV.")
    parser.add_argument("pdf_path", help="Path to the LinkedIn-exported PDF")
    parser.add_argument("--output", default="output/profile_data.csv", help="Output CSV file")
    args = parser.parse_args()
    main(args.pdf_path, args.output)

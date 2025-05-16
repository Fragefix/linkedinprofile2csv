# LinkedIn PDF Profile Parser

This Python script extracts key details from a PDF-exported LinkedIn profile and saves them into a structured CSV file.

## 🔧 Features

- Extracts: Name, Headline, Location, About, Experience, Education, Skills, Certifications, Languages, Projects
- Outputs a single CSV row per profile
- Command-line usage

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

```bash
python linkedin_pdf_parser.py /path/to/profile.pdf --output output/profile_data.csv
```

Default output path is `output/profile_data.csv`.

## 📂 Output Format

CSV columns include:
- Name
- Headline
- Location
- About
- Experience
- Education
- Skills
- Licenses & Certifications
- Languages
- Projects

## 🧠 Notes

This parser assumes a typical LinkedIn PDF layout. Formatting may vary depending on export version and user input.

## 📄 License

MIT

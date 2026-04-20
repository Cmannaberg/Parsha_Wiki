import pdfplumber
import os
import json

# The folder where the PDF files are located
pdf_folder = "/Users/carymannaberg/Parsha_Through_Midrash"

# Get only PDF files in the folder
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
print (f"Found {len(pdf_files)} PDF files:")

#loop through the PDF files and extract text from each one
all_text = {}
for filename in pdf_files:
    full_path = os.path.join(pdf_folder, filename)
    pages = []

    try:
        with pdfplumber.open(full_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                   pages.append(page_text)

        all_text[filename] = pages
        print(f"-Extracted: {filename}")

    except Exception as e:
        print(f"- SKIPPED: {filename}: ({e})")  

print(f"\nDone! Extracted text from {len(all_text)} files.")


with open("parsha_text.json", "w") as f:
    json.dump(all_text, f)

print("Saved to parsha_text.json")




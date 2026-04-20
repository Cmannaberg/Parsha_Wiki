# Parsha Through Midrash — Search Wiki

A local search tool for exploring Torah portion study handouts 
prepared by Rabbi Micah Streiffer.

## What it does
- Searches across 39 Parsha study handouts
- Shows snippets of text where your search term appears
- Click any result to open the original PDF

## Requirements
- Python 3.x
- PDF handouts in a local folder

## Setup

1. Clone this repo
2. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install libraries:
   pip install pdfplumber whoosh flask

4. Update the pdf_folder path in extract.py and app.py 
   to point to your PDF folder

5. Extract and index the PDFs:
   python3 extract.py
   python3 index.py

6. Run the app:
   python3 app.py

7. Open your browser to:
   http://127.0.0.1:5000

## Built with
- pdfplumber
- Whoosh
- Flask
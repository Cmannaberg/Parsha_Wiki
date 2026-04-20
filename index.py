import json
import os
from whoosh import index
from whoosh.fields import Schema, TEXT, ID, NUMERIC

# Define the structure of our search index
schema = Schema(
    filename=ID(stored=True),
    page_num=NUMERIC(stored=True),
    content=TEXT(stored=True)
)

# Create a folder to store the index
index_dir = "search_index"
os.makedirs(index_dir, exist_ok=True)

# Create the index
ix = index.create_in(index_dir, schema)

# Load our extracted text
with open("parsha_text.json", "r") as f:
    all_text = json.load(f)

# Add each page of each Parsha to the index
writer = ix.writer()

for filename, pages in all_text.items():
    for page_num, text in enumerate(pages, start=1):
        writer.add_document(
            filename=filename,
            page_num=page_num,
            content=text
        )
    print(f"- Indexed: {filename}")

writer.commit()
print(f"\nDone! Indexed {len(all_text)} files.")
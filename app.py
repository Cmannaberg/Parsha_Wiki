from flask import Flask, request, render_template, send_file
from whoosh import index
from whoosh.qparser import QueryParser
import os

app = Flask(__name__)

#Where your PDF's are located
pdf_folder = "/Users/carymannaberg/Parsha_Through_Midrash"

#Open the search index
ix = index.open_dir("search_index")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query_text = request.args.get("q", "")
    results = []

    if query_text:
        with ix.searcher() as searcher:

            query = QueryParser("content", ix.schema).parse(query_text)
            hits = searcher .search(query, limit=20)
            for hit in hits:
                results.append({
                    "filename": hit["filename"],
                    "page_num": hit["page_num"],
                    "snippet": hit.highlights("content")
                })
    return render_template("results.html", query=query_text, results=results)

@app.route("/open/<filename>")
def open_pdf(filename):
    full_path = os.path.join(pdf_folder, filename)
    return send_file(full_path, mimetype="application/pdf")


if __name__ == "__main__":
    app.run(debug=True)
    
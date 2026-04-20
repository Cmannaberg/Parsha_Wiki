from whoosh import index
from whoosh.qparser import QueryParser

#open the index
ix = index.open_dir("search_index")

#search for a word
search_term = "talmud"

with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse(search_term)
    results = searcher.search(query)
    
    print(f"Results for '{search_term}':")
    for result in results:
        print(f"- {result['filename']}")

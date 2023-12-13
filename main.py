from mongodb_cloud import embed_plots_in_collection
from mongodb_cloud import vectorSearch

search_term = "Thriller"
search_results = vectorSearch(search_term)

for doc in search_results:
    print(f"Movie name: {doc['title']}, \nMovie plot: {doc['plot']}\n")
    

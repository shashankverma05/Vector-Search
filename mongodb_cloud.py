import pymongo
import os
from vector_embeddings import query


# print(os.environ.get("MONGO_HOST"))
client = pymongo.MongoClient(os.environ.get("MONGO_HOST"))
db = client.sample_mflix
collection = db.movies

"""
items = collection.find().limit(5)
print(items)
for item in items:
    print(item)
    break
"""

def embed_plots_in_collection(collection):
    try:

        for doc in collection.find({"plot":{"$exists": True}}).limit(50):
            # print(doc["plot"])
            doc["plot_embedding"] = query({"inputs" : doc["plot"]}) 
            collection.replace_one({'_id': doc['_id']}, doc)
        
    except Exception as ex:
        print(ex)

embed_plots_in_collection(collection)
# print(query({"inputs":movie_plot}))


def vectorSearch(search_term):
    results = collection.aggregate([
        {
            "$vectorSearch":{
                "queryVector":query(search_term),
                "path": "plot_embedding",
                "numCandidates":100,
                "limit":4,
                "index":"plotSemanticSearch"
            
            }
        }
    ])
    return results
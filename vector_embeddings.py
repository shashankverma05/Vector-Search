# Feature Extraction - Vector Embeddings

import requests
import os

HUGGING_FACE_TOKEN = os.environ.get('HUGGING_FACE_VECTOR_SEARCH_TOKEN')
API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}

def query(payload):

    ''' Returns Vector Embeddings '''
    
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise ValueError(f"Error: {response.status_code}:{response.text}")
    return response.json()

# print(query({"inputs": "Shashank Verma"}))
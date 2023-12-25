from googlesearch import search
import json
import requests
from bs4 import BeautifulSoup
import re
from transformers import pipeline
# Function to perform Google search and get top URLs
def google_search(query, max_links=5, time_delay=2):
    results = []
    try:
        for result in search(query, num=max_links, stop=max_links, pause=time_delay):
            results.append({'title': f"Result {len(results)+1}", 'link': result})
        return results

    except Exception as e:
        print(f"An error occurred for '{query}': {type(e).__name__} - {e}")
        return None

# Function to extract text from URLs
def extract_text(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = ' '.join([p.get_text() for p in soup.find_all('p')])
            return text
        else:
            return f"Failed to fetch data from {url}"
    except Exception as e:
        return f"Error occurred: {type(e).__name__} - {e}"

# Function for semantic search using Transformers
def semantic_search(query, texts):
    qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
    for text in texts:
        result = qa_pipeline(question=query, context=text)
        if result['score'] > 0.1:  # Adjust threshold as needed
            return result['answer']
    return "No relevant information found."

# Main script
queries = [
    "Current president of India?"
]
max_links_per_query = 3
time_delay_between_queries = 5
all_results = {}

for query in queries:
    results = google_search(query, max_links=max_links_per_query, time_delay=time_delay_between_queries)
    if results is not None:
        all_results[query] = {'links': results, 'information': None}
        urls = [link['link'] for link in results]
        extracted_texts = [extract_text(url) for url in urls]
        answer = semantic_search(query, extracted_texts)
        all_results[query]['information'] = answer

json_results = json.dumps(all_results, indent=2)
print(json_results)

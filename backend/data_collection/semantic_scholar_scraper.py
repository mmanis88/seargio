# semantic_scholar_scraper.py
import requests

SEMANTIC_SCHOLAR_API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def fetch_semantic_scholar_papers(query, limit=10):
    params = {
        'query': query,
        'fields': 'title,abstract,authors,year,externalIds',
        'limit': limit
    }
    headers = {
        'x-api-key': 'YOUR_API_KEY'  # Get an API key from Semantic Scholar
    }
    
    response = requests.get(SEMANTIC_SCHOLAR_API_URL, params=params, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch Semantic Scholar papers: {response.status_code}")
    
    return response.json().get('data', [])

# Example usage
if __name__ == "__main__":
    query = "artificial intelligence"
    papers = fetch_semantic_scholar_papers(query, limit=5)
    for paper in papers:
        print(paper)

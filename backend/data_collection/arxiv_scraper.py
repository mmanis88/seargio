# arxiv_scraper.py
import requests
import xml.etree.ElementTree as ET

ARXIV_API_URL = "http://export.arxiv.org/api/query"

def fetch_arxiv_papers(query, max_results=10):
    params = {
        'search_query': query,
        'start': 0,
        'max_results': max_results
    }
    response = requests.get(ARXIV_API_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch arXiv papers: {response.status_code}")
    
    # Parse the XML response
    root = ET.fromstring(response.content)
    
    papers = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        paper = {
            'title': entry.find("{http://www.w3.org/2005/Atom}title").text,
            'summary': entry.find("{http://www.w3.org/2005/Atom}summary").text,
            'authors': [author.find("{http://www.w3.org/2005/Atom}name").text for author in entry.findall("{http://www.w3.org/2005/Atom}author")],
            'published': entry.find("{http://www.w3.org/2005/Atom}published").text,
            'link': entry.find("{http://www.w3.org/2005/Atom}id").text
        }
        papers.append(paper)
    
    return papers

# Example usage
if __name__ == "__main__":
    query = "machine learning"
    papers = fetch_arxiv_papers(query, max_results=5)
    for paper in papers:
        print(paper)

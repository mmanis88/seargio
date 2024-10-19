# pubmed_scraper.py
import requests
from xml.etree import ElementTree

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_DB = "pubmed"

def fetch_pubmed_paper_ids(query, max_results=10):
    params = {
        'db': PUBMED_DB,
        'term': query,
        'retmax': max_results,
        'retmode': 'xml'
    }
    response = requests.get(PUBMED_API_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch PubMed paper IDs: {response.status_code}")
    
    # Parse the XML response
    root = ElementTree.fromstring(response.content)
    ids = [id_elem.text for id_elem in root.findall(".//Id")]
    return ids

def fetch_pubmed_paper_details(paper_id):
    params = {
        'db': PUBMED_DB,
        'id': paper_id,
        'retmode': 'xml'
    }
    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch PubMed paper details: {response.status_code}")
    
    # Parse the XML response
    root = ElementTree.fromstring(response.content)
    paper = {
        'title': root.find(".//Item[@Name='Title']").text,
        'authors': root.find(".//Item[@Name='AuthorList']").text,
        'source': root.find(".//Item[@Name='Source']").text,
        'pubdate': root.find(".//Item[@Name='PubDate']").text,
        'doi': root.find(".//Item[@Name='DOI']").text
    }
    return paper

# Example usage
if __name__ == "__main__":
    query = "deep learning"
    paper_ids = fetch_pubmed_paper_ids(query, max_results=5)
    for paper_id in paper_ids:
        paper_details = fetch_pubmed_paper_details(paper_id)
        print(paper_details)

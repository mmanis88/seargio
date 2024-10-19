# test_apis.py
import unittest
from arxiv_scraper import fetch_arxiv_papers
from semantic_scholar_scraper import fetch_semantic_scholar_papers
from pubmed_scraper import fetch_pubmed_paper_ids, fetch_pubmed_paper_details

class TestAPIs(unittest.TestCase):
    
    def test_arxiv_api(self):
        """Test if the arXiv API is working by fetching papers."""
        query = "machine learning"
        result = fetch_arxiv_papers(query, max_results=1)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0, "No results returned from arXiv API")
        self.assertIn('title', result[0], "No title found in arXiv paper")

    def test_semantic_scholar_api(self):
        """Test if the Semantic Scholar API is working by fetching papers."""
        query = "artificial intelligence"
        result = fetch_semantic_scholar_papers(query, limit=1)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0, "No results returned from Semantic Scholar API")
        self.assertIn('title', result[0], "No title found in Semantic Scholar paper")

    def test_pubmed_api(self):
        """Test if the PubMed API is working by fetching paper IDs and details."""
        query = "deep learning"
        paper_ids = fetch_pubmed_paper_ids(query, max_results=1)
        self.assertIsInstance(paper_ids, list)
        self.assertGreater(len(paper_ids), 0, "No results returned from PubMed API")
        
        # Fetch details for the first paper
        paper_details = fetch_pubmed_paper_details(paper_ids[0])
        self.assertIsInstance(paper_details, dict)
        self.assertIn('title', paper_details, "No title found in PubMed paper details")

if __name__ == "__main__":
    unittest.main()

import sys, os
import pytest
import asyncio

# Adjust path so CertUaScraper can be imported from its directory.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scraipe-cyber/ukraine"))
from scraipe_cyber.ukraine import CertUaScraper

@pytest.mark.asyncio
async def test_invalid_url():
    # ...existing setup code...
    scraper = CertUaScraper()
    result = await scraper.async_scrape("invalid")
    assert not result.success, f"Expected failure but got: {result}"
    assert "Invalid URL" in result.error

@pytest.mark.asyncio
async def test_live_article_id():
    # Live test: using a valid numeric article id extracted from the example URL.
    scraper = CertUaScraper()
    result = await scraper.async_scrape("6282069")
    assert result.success, f"Live scrape failed: {result.message}"
    assert isinstance(result.content, str) and len(result.content) > 0

@pytest.mark.asyncio
async def test_live_full_url():
    # Live test: using a valid full URL.
    scraper = CertUaScraper()
    result = await scraper.async_scrape("https://cert.gov.ua/article/6282069")
    assert result.success, f"Live scrape failed: {result.message}"
    assert isinstance(result.content, str) and len(result.content) > 0
    assert "id" in result.metadata
    assert result.metadata["id"] == "6282069"
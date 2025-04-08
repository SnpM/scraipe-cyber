from scraipe_cyber.ukraine.ukraine_cyber_multi_scraper import UkraineCyberMultiScraper
from scraipe import ScrapeResult,IScraper
from scraipe.extended import TelegramMessageScraper
import pytest
import dotenv
import os

class DummyTelegramScraper(IScraper):
    def scrape(self, url: str) -> ScrapeResult:
        # Simulate scraping a Telegram message
        return ScrapeResult.succeed(url, content="Dummy Telegram content")
    def get_expected_link_format(self):
        return TelegramMessageScraper.get_expected_link_format(self)
    
@pytest.fixture
def scraper():
    """Fixture to create an instance of UkraineCyberMultiScraper with a dummy telegram_message_scraper."""
    dummy_telegram_scraper = DummyTelegramScraper()
    return UkraineCyberMultiScraper(dummy_telegram_scraper)

@pytest.fixture
def live_scraper():
    """Fixture that loads environment variables for live testing."""
    import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    # Extract necessary environment variables
    try:
        name = os.getenv("TELEGRAM_NAME")
        api_id = os.getenv("TELEGRAM_API_ID")
        api_hash = os.getenv("TELEGRAM_API_HASH")
        phone_number = os.getenv("TELEGRAM_PHONE_NUMBER")
    except KeyError as e:
        pytest.skip(f"Missing environment variable for live test: {e}")

    # Create an instance of TelegramMessageScraper with the loaded credentials
    telegram_message_scraper = TelegramMessageScraper(
        name=name,
        api_id=api_id,
        api_hash=api_hash,
        phone_number=phone_number
    )
    return UkraineCyberMultiScraper(telegram_message_scraper)

# Offline tests:
def test_offline_cert_ua(scraper):
    # live test using cert.gov.ua link in offline mode
    url = "https://cert.gov.ua/article/6282069"
    result = scraper.scrape(url)
    assert result, "Offline: Failed to process cert.gov.ua link"

def test_offline_telegram(scraper):
    # live test using Telegram link in offline mode
    url = "https://t.me/TelegramTips/516"
    result = scraper.scrape(url)
    assert result, "Offline: Failed to process Telegram link"

def test_offline_text_scraper(scraper):
    # live test using fallback text scraper link (AP News) in offline mode
    url = "https://apnews.com/article/dire-wolf-colossal-biosciences-de-extinction-56d6c192c5d968731b448081aa4149fe"
    result = scraper.scrape(url)
    assert result, "Offline: Failed to process AP News link"

# Live tests:
# Note: These tests require valid credentials and network access to run successfully.
# Run with pytest -s the first time to authenticate the Telegram client.
def test_live_cert_ua(live_scraper):
    # live test using cert.gov.ua link with live credentials
    url = "https://cert.gov.ua/article/6282069"
    result = live_scraper.scrape(url)
    assert result, "Live: Failed to process cert.gov.ua link"

def test_live_telegram(live_scraper):
    # live test using Telegram link with live credentials
    url = "https://t.me/TelegramTips/516"
    result = live_scraper.scrape(url)
    assert result, "Live: Failed to process Telegram link"

def test_live_text_scraper(live_scraper):
    # live test using fallback text scraper link (AP News) with live credentials
    url = "https://apnews.com/article/dire-wolf-colossal-biosciences-de-extinction-56d6c192c5d968731b448081aa4149fe"
    result = live_scraper.scrape(url)
    assert result, "Live: Failed to process AP News link"


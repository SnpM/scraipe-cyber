# Import components
from scraipe_cyber.ukraine import UkraineCyberMultiScraper
from scraipe.defaults import TextStatsAnalyzer
from scraipe.extended import TelegramMessageScraper
from scraipe import Workflow
import os
import dotenv

# Initialize the TelegramMessageScraper with credentials from environment variables
# Configure and run `source ukraine_example_secrets.env` to set up the environment variables
dotenv.load_dotenv()
try:
    name = os.getenv("TELEGRAM_NAME")
    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    phone_number = os.getenv("TELEGRAM_PHONE_NUMBER")
except KeyError as e:
    raise ValueError(f"Missing environment variable for live test: {e}")
# Create an instance of TelegramMessageScraper with the loaded credentials
# This may prompt your telegram account for a login code in the console
telegram_message_scraper = TelegramMessageScraper(
    name=name,
    api_id=api_id,
    api_hash=api_hash,
    phone_number=phone_number
)

# Initialize the scraper and analyzer
scraper = UkraineCyberMultiScraper(telegram_message_scraper)
analyzer = TextStatsAnalyzer()

# Create the workflow instance
workflow = Workflow(scraper, analyzer)

# List urls to scrape
urls = [
    "https://t.me/TelegramTips/516",
    "https://cert.gov.ua/article/6282069",
    "https://apnews.com/article/dire-wolf-colossal-biosciences-de-extinction-56d6c192c5d968731b448081aa4149fe"
]

# Run the workflow
workflow.scrape(urls)
workflow.analyze()

# Print the results
results = workflow.export()
print(results)
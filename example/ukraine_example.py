# Import components
from scraipe_cyber.ukraine import UkraineCyberMultiScraper
from scraipe.defaults import TextStatsAnalyzer
from scraipe.extended import TelegramMessageScraper
from scraipe import Workflow
import os
import dotenv

# NOTE: a template `secrets.env.template` file is provided that should be renamed to `secrets.env`
# Configure and run `source secrets.env` to load credentials from environment variables
dotenv.load_dotenv()
try:
    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    phone_number = os.getenv("TELEGRAM_PHONE_NUMBER")
except KeyError as e:
    raise ValueError(f"Missing environment variable for live test: {e}")

# Create an instance of TelegramMessageScraper with the loaded credentials
# This may prompt your telegram account for a login code in the console
telegram_message_scraper = TelegramMessageScraper(
    api_id=api_id,
    api_hash=api_hash,
    phone_number=phone_number,
    session_name="ukraine_example_session",
)

# Initialize the scraper and analyzer
scraper = UkraineCyberMultiScraper(telegram_message_scraper)
analyzer = TextStatsAnalyzer()

# Create the workflow instance
workflow = Workflow(scraper, analyzer)

# List urls to scrape
urls = [
    "https://t.me/TelegramTips/12345678",
    "https://t.me/random_name_1234/567",
    "https://t.me/TelegramTips/516",
    "https://cert.gov.ua/article/6282069",
    "https://apnews.com/article/dire-wolf-colossal-biosciences-de-extinction-56d6c192c5d968731b448081aa4149fe"
]

# Run the workflow
workflow.scrape(urls)
workflow.analyze()

# Print the results
results = workflow.export(verbose=True)
print(results)
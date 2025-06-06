# scraipe-cyber
[![pypi](https://img.shields.io/pypi/v/scraipe-cyber.svg)](https://pypi.python.org/pypi/scraipe-cyber)
[![versions](https://img.shields.io/pypi/pyversions/scraipe-cyber.svg)](https://github.com/SnpM/scraipe-cyber)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/SnpM/scraipe-cyber/blob/main/LICENSE)

Scraipe scrapers for cyber research. Features UkraineCyberMultiScraper which orchestrates news article, Cert UA API, and Telegram scraping.

## Installation

Ensure you have Python>=3.10 installed. Run `pip install scraipe-cyber`.

## Example Usage

```python
# Configure a TelegramMessageScraper to use within a UkraineCyberMultiScraper
telegram_scraper = TelegramMessageScraper(telegram_api_id, telegram_api_hash, telegram_phone_number, session_name="my_session")
ukraine_scraper = UkraineCyberMultiScraper(telegram_message_scraper=telegram_scraper)
```

ukraine_scraper can be plugged into a [Scraipe workflow](UkraineCyberMultiScraper).

See [ukraine_europoc_research.ipynb](./example/ukraine_europoc_research.ipynb) for a use case with LLM location extraction.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request for improvements.

## Maintainer

This project is maintained by [nibs](https://github.com/SnpM).
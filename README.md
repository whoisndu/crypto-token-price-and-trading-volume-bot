# crypto-token-price-and-trading-volume-bot

**Crypto Price Bot**

Crypto Price Bot is a Telegram bot that provides the price and trading volume of cryptocurrencies. It utilizes the CoinGecko API to fetch real-time data.

## Features

- Retrieve the price and trading volume of cryptocurrencies
- Supports multiple tickers in a single command
- Error handling for invalid ticker symbols or API issues

## Setup

1. Clone the repository:
```
   git clone https://github.com/your-username/crypto-price-bot.git
```
2. Install the required dependencies: ``` pip install -r requirements.txt ```
3. Obtain a Telegram bot token: 
- Create a new bot on Telegram using the BotFather.
- Copy the generated bot token.
- Replace the placeholder in the code:
4. Open crypto_price_bot.py in a text editor.
5. Replace "YOUR_TELEGRAM_BOT_TOKEN" with the Telegram bot token you obtained in the previous step.

**Usage**
1. Start the bot by running the following command: ```python crypto_price_bot.py```
2. Open Telegram and search for your bot.
3. Send the /start command to the bot to receive the welcome message and instructions.
4. Use the /price command followed by one or more cryptocurrency ticker symbols to retrieve their price and trading volume. For example: ```/price btc eth ada```

**License**
This project is licensed under the MIT License.


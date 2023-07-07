# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:03:46 2023

@author: NDU-PC
"""

import os
import requests
from telegram.ext import Updater, CommandHandler

# CoinGecko API base URL
API_BASE_URL = "https://api.coingecko.com/api/v3"

# Telegram bot token
TOKEN = "6328617871:AAHY5Ufd2LVNUVzYiIyQCGYypUCfHre5tCg"

# Function to get cryptocurrency price and trading volume
def get_crypto_info(ticker):
    url = f"{API_BASE_URL}/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": ",".join(ticker),
        "order": "market_cap_desc",
        "per_page": 1,
        "page": 1,
        "sparkline": False,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if isinstance(data, list) and len(data) > 0:
        price = data[0].get("current_price")
        volume = data[0].get("total_volume")
        return price, volume
    else:
        error_message = (
            data.get("error", "Unknown error")
            if isinstance(data, dict)
            else "Unknown error"
        )
        print(f"CoinGecko API Error: {error_message}")
        print(f"API Response: {response.text}")
    return None, None


# Telegram bot command handler
def crypto_price(update, context):
    tickers = context.args
    responses = []
    for ticker in tickers:
        ticker = ticker.lower()
        price, volume = get_crypto_info([ticker])
        if price is not None and volume is not None:
            response = f"Price of {ticker.upper()}: ${price:.2f}\nTrading Volume: ${volume:.2f}"
        else:
            response = f"Unable to retrieve information for {ticker.upper()}."
            print(f"Error: {response}")
        responses.append(response)
    update.message.reply_text("\n\n".join(responses))


# Telegram bot error handler
def error(update, context):
    print(f"Error: {context.error}")


# Telegram bot start handler
def start(update, context):
    welcome_message = (
        "Welcome to the Crypto Price Bot!\n"
        "To get the price and trading volume of cryptocurrencies, use the /price command followed by one or more ticker symbols.\n"
        "For example, type /price btc eth ada"
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=welcome_message
    )


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", crypto_price))
    dp.add_error_handler(error)
    updater.start_polling()
    print("Bot is running...")
    updater.idle()


if __name__ == "__main__":
    main()

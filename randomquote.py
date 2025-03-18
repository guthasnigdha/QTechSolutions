import requests
import random

# Local list of quotes (fallback when API is unavailable)
local_quotes = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "Happiness depends upon ourselves. - Aristotle",
    "In the middle of every difficulty lies opportunity - Albert Einstein"
]

# Function to fetch a quote from the API
def fetch_quote_from_api():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    except requests.exceptions.RequestException:
        return None  # If API call fails, return None

# Function to get a random quote (API first, then fallback to local)
def get_random_quote():
    quote = fetch_quote_from_api()
    if quote is None:  # If API fails, use local quotes
        quote = random.choice(local_quotes)
    return quote

# Main loop for user interaction
while True:
    input("Press Enter to get a random quote (or type 'exit' to quit): ")
    print("\n✨ Quote: " + get_random_quote() + "\n")
    if input("Type 'exit' to quit, or press Enter to continue: ").lower() == "exit":
        break

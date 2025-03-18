import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://open.er-api.com/v6/latest"

    def convert_currency(self, amount, from_currency, to_currency):
        try:
            response = requests.get(f"{self.base_url}/{from_currency}", params={"apikey": self.api_key})
            response.raise_for_status()
            data = response.json()
            
            if to_currency not in data["rates"]:
                print(f"Error: Invalid target currency '{to_currency}'.")
                return
            
            exchange_rate = data["rates"][to_currency]
            converted_amount = amount * exchange_rate
            print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        except requests.exceptions.HTTPError as e:
            print(f"Error: Unable to fetch exchange rates. {e}")
        except KeyError:
            print("Invalid currency code or data format. Please try again.")

def main():
    api_key = "4aef56a28d622bb181faf915336fd3f6"  
    converter = CurrencyConverter(api_key)

    while True:
        print("\nCurrency Converter")
        print("1. Convert Currency")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter the amount: "))
                from_currency = input("Enter the source currency (e.g., USD): ").upper()
                to_currency = input("Enter the target currency (e.g., EUR): ").upper()
                converter.convert_currency(amount, from_currency, to_currency)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == "2":
            print("Exiting Currency Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"  # For temperature in Celsius; use "imperial" for Fahrenheit
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]

            print(f"\nWeather in {city_name}, {country}:")
            print(f"Temperature: {temp}°C")
            print(f"Condition: {weather.capitalize()}")
        except requests.exceptions.HTTPError as err:
            print(f"Error: Unable to fetch weather data. {err}")
        except KeyError:
            print("Invalid city name. Please try again.")

def main():
    api_key = "ff2db94d72bed997bc599259ed113856"  # Replace with your OpenWeatherMap API key
    weather_app = WeatherApp(api_key)

    while True:
        print("\nWeather Application")
        print("1. Get Weather by City")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            city = input("Enter city name: ")
            weather_app.get_weather(city)
        elif choice == "2":
            print("Exiting Weather Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

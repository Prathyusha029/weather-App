import requests
def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        icon_code = data['weather'][0]['icon']
        print("\n" + "="*50)
        print(f"🌤️Weather App")
        print("="*50)
        print(f"Location: {city}, {country}")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"🤔 Feels Like: {feels_like}°C")
        print(f"💧Humidity: {humidity}%")
        print(f"🌤️ Condition: {description.capitalize()}")
        print("="*50)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except KeyError:
        print("Invalid location. Please check the city name or ZIP code.")
if __name__ == "__main__":
    api_key = "9356b62e672abdd9358633bb66580058"
    location = input("Enter a city name or ZIP code: ")
    get_weather(api_key, location)

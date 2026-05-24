

import requests
import json
import sys
from tabulate import tabulate


class Weather:
    def __init__(self):
        self.data = self.get_data()
        self.weather = self.get_weather()

    def get_data(self):
        if len(sys.argv) != 2:

            sys.exit("Man shut ur b** ass upp!")
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={sys.argv[1].capitalize()}&units=metric&appid=1fe90014633fd5a388324f2fdfef9237"
        )
        data = data.json()
        return data

    def get_weather(self):
        try:
            description = self.data["weather"][0]["description"]
            city_name = self.data["name"]
            temp = self.data["main"]["temp"]
            feels_like = self.data["main"]["feels_like"]
            humidity = self.data["main"]["humidity"]
        except KeyError:
            sys.exit("Bagul dolbaeb")
        idk = [
            {
                "Description": description.title(),
                "City": city_name.title(),
                "Temperature": f"{temp}°C",
                "Feels Like": f"{feels_like}°C",
                "Humidity": f"{humidity}%",
            }
        ]
        return idk

    def show(self):
        print(tabulate(self.weather, headers="keys", tablefmt="rounded_grid"))


def main():
    weather = Weather()
    weather.show()


if __name__ == "__main__":
    main()

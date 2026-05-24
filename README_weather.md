# Weather CLI

A simple Python command-line tool that fetches and displays current weather for any city using the OpenWeatherMap API.

---

## Features

- Fetches live weather data by city name
- Displays temperature, feels like, humidity, and weather description
- Clean formatted table output in the terminal
- Handles invalid city names and missing arguments gracefully

---

## Requirements

- Python 3.10+
- `requests`
- `tabulate`

Install dependencies:

```bash
pip install requests tabulate
```

---

## Usage

```bash
python weather.py <city>
```

**Example:**

```bash
python weather.py London
```

**Output:**

```
╭─────────────┬─────────┬─────────────┬────────────┬──────────╮
│ Description │ City    │ Temperature │ Feels Like │ Humidity │
├─────────────┼─────────┼─────────────┼────────────┼──────────┤
│ Clear Sky   │ London  │ 18.4°C      │ 17.1°C     │ 62%      │
╰─────────────┴─────────┴─────────────┴────────────┴──────────╯
```

---

## Notes

- Requires a free OpenWeatherMap API key — sign up at [openweathermap.org](https://openweathermap.org)
- Temperature displayed in Celsius by default
- Replace the API key in the source with your own before use

---

Fully written by hand in Python as part of a personal projects portfolio.

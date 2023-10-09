"""Get weather"""
import requests
import subprocess
import math
import sys

CONDITIONS = {1000: "Clear",
              1100: "Mostly Clear",
              1101: "Partly Cloudy",
              1102: "Mostly Cloudy",
              1001: "Cloudy",
              1103: "Mostly Clear",
              2100: "Light Fog",
              2000: "Fog",
              2101: "Light Fog",
              4200: "Light Rain",
              "N/A": "N/A"}


def get_weather(coordinates: str, fetch: str) -> str:
    url = f"https://api.tomorrow.io/v4/timelines?location={coordinates}&fields=temperature,weatherCode&timesteps=1h&units=metric&apikey=<YOUR API KEY HERE>"

    try:
        response = requests.get(url).json()["data"]["timelines"][0]["intervals"][0]["values"]
    except KeyError:
        return "N/A"

    return math.ceil(response[fetch])


OPTIONS = {"temperature": lambda coordinates: str(get_weather(coordinates, "temperature")) + "°C",
           "weathercode": lambda coordinates: CONDITIONS[get_weather(coordinates, "weatherCode")]}

subprocess.call(["echo", f"{OPTIONS[sys.argv[1:][0]]('<YOUR CITY COORDINATES HERE>')}"])

import requests


def get_weather_for_city(city):

    url = f"http://wttr.in/{city}"
    params = {"lang": "ru", "m": "", "M": "", "n": "", "q": "", "T": ""}
    headers = {"User-Agent": "curl"}
    
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.text


def main():

    cities = ["Лондон", "Шереметьево", "Череповец"]
    
    for city in cities:
        weather_text = get_weather_for_city(city)
        print(weather_text)


if __name__ == "__main__":
    main()

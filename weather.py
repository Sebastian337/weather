import requests


def get_weather():
    url_template = "http://wttr.in/{}"
    cities = ["Лондон", "Шереметьево", "Череповец"]
    params = {"lang": "ru", "m": "", "M": "", "n": "", "q": "", "T": ""}
    headers = {"User-Agent": "curl"}

    for city in cities:
        url = url_template.format(city)
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    get_weather()
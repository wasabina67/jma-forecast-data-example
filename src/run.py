import requests


def main():
    code = "130000"
    overview_forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{code}.json"
    forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{code}.json"

    resp = requests.get(overview_forecast_url)
    resp_json = resp.json()
    print(resp_json)

    resp = requests.get(forecast_url)
    resp_json = resp.json()
    print(resp_json)


if __name__ == "__main__":
    main()

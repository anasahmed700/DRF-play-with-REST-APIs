import requests

def main():
    payload = {"base": "USD", "symbols": "GBP"}
    response = requests.get('https://api.exchangeratesapi.io/latest', params=payload)

    if response.status_code != 200:
        print('Status code: ', response.status_code)
        raise Exception("There was some error!")

    else:
        data = response.json()
        print("Data: ", data)
        print("GBP rates: ", data['rates']['GBP'])

if __name__ == "__main__":
    main()
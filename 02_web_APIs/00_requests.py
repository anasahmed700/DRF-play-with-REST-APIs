import requests

def main():
    response = requests.get('http://www.google.com')
    
    print('headers: ', response.headers)
    print('Status code: ', response.status_code)
    print('Content type:', response.headers['Content-Type'])


if __name__ == "__main__":
    main()
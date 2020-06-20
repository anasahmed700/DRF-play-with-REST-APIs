import requests


def client():
    # credentials = {'username': 'admin', 'password': 'admin'}
    """first send post request with credentials to get auth token key in response"""
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)
    """then make a get request with that token as headers to the required api endpoint"""
    token = 'Token 25a42c27db93dffb807aa2f901416e89cc8caf81'
    headers = {'Authorization': token}
    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    print("Status code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()

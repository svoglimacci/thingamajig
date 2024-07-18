import requests
from requests.exceptions import HTTPError, RequestException, ReadTimeout


def fetch(url, **kwargs):

    headers = {}
    params = {}
    timeout = 3

    for key, value in kwargs.items():
        if key == "headers":
            headers = value
        elif key == "timeout":
            timeout = value
        elif key == "params":
            params = value

    try:
        response = requests.get(url, headers=headers, params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")

    except ReadTimeout as req_err:
        print(f"Request error occurred: {req_err}")

    except RequestException as req_err:
        print(f"Request error occurred: {req_err}")

    return None

import requests


def send_get_request(url: str, payload: dict):
    """
    Arguements:
        url (str): API Endpoint
        payload (dict): API Filters

    Returns:
        requests.response: HTTPS response object
    """

    resp = requests.get(url, params=payload)
    return resp


def _validate_response(resp: requests.Response):
    if resp.status_code == 200:
        return True
    else:
        print(resp.status_code)
        print(resp.text)
        return False

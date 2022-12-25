from typing import Tuple, List
from rick_morty_client.utils import send_get_request, _validate_response
from rick_morty_client.constants import API_ENDPOINTS


def query_character(
    name: str = None,
    page: int = None,
    id: int = None,
    status: str = None,
    species: str = None,
    type: str = None,
    gender: str = None,
    origin: Tuple[str] = None,
    location=None,
    image: str = None,
    url: List[str] = None,
    create: str = None,
) -> dict:

    """
    Arguments:
        status (str): The status of the character ('Alive', 'Dead' or 'unknown').
        gender (str): The gender of the character ('Female', 'Male', 'Genderless' or 'unknown').
    Returns:
        dict: response object converted to dict

    Note:
        - Find more information here: https://rickandmortyapi.com/documentation#episode

    Todo:
        - Add def for all args
    """

    payload = {
        "name": name,
        "page": page,
        "id": id,
        "status": status,
        "species": species,
        "type": type,
        "gender": gender,
        "origin": origin,
        "location": location,
        "image": image,
        "url": url,
        "create": create,
    }

    resp = send_get_request(API_ENDPOINTS["character"], payload)
    if _validate_response(resp):
        return resp.json()
    else:
        print("not working")

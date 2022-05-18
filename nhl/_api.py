from typing import Dict

import requests

BASE = "https://statsapi.web.nhl.com/api/v1"


def fetch(url: str) -> Dict:
    """
    Fetchs a URL from the NHL statsapi and returns its JSON.
    """
    full_url = f"{BASE}/{url}"
    response = requests.get(full_url)

    if not response.ok:
        raise Exception(f"Failed to fetch {full_url}. Status code: {response.status_code}. Reason: {response.reason}.")

    return response.json()

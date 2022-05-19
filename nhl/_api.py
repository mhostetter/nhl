from typing_extensions import Literal

import requests

STATSAPI_BASE = "https://statsapi.web.nhl.com/api/v1"
HTMLREPORTS_BASE = "https://www.nhl.com/scores/htmlreports"


def fetch(sub_url: str, base: Literal["statsapi", "htmlreports"] = "statsapi") -> requests.Response:
    """
    Fetches a web response.
    """
    if base == "statsapi":
        url = f"{STATSAPI_BASE}/{sub_url}"
    else:
        url = f"{HTMLREPORTS_BASE}/{sub_url}"
    response = requests.get(url)

    if not response.ok:
        raise Exception(f"Failed to fetch {response.url}. Status code: {response.status_code}. Reason: {response.reason}.")

    return response

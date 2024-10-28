import requests

# A few handy JSON types
JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

def http_get(url: str) -> JSONObject:
    response = requests.get(url)
    return response.json()

BASE_OPEN_BREWERY_DB_URL = "https://api.openbrewerydb.org/v1/breweries"

## Creating functions for each endpoint at Open Brewery DB
def get_single_brewery(obdb_id: str) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}/{obdb_id}")


def get_breweries_list(limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?per_page{limit}")


def get_breweries_by_city(city: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_city={city}&per_page={limit}")


def get_breweries_by_country(country: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_city={country.replace(' ', '%20')}&per_page={limit}")


def get_breweries_by_state(state: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_state={state.replace(' ', '%20')}&per_page={limit}")


def get_breweries_by_postal(postal: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_postal={postal}&per_page={limit}")


def get_breweries_by_distance(lat: float, long: float, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_dist={str(lat)},{str(long)}&per_page={limit}")


def get_breweries_by_ids(id_list: list[str]) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_ids={','.join(id_list)}")


def get_breweries_by_name(name: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_ids={'_'.join(name)}&per_page={limit}")


def get_breweries_by_type(brewery_type: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_type={brewery_type}&per_page={limit}")


def get_brewery_random() -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}/random")
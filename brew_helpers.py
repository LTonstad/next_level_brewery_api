import requests

BASE_OPEN_BREWERY_DB_URL = "https://api.openbrewerydb.org/v1/breweries"
META_OPEN_BREWERY_DB_URL = "https://api.openbrewerydb.org/v1/breweries/meta"
BREWERY_TYPES = {
    "micro" : "Most craft breweries. For example, Samual Adams is still considered a micro brewery.",
    "nano" : "An extremely small brewery which typically only distributes locally.",
    "regional" : "A regional location of an expanded brewery. Ex. Sierra Nevada’s Asheville, NC location.",
    "brewpub" : "A beer-focused restaurant or restaurant/bar with a brewery on-premise.",
    "large" : "A very large brewery. Likely not for visitors. Ex. Miller-Coors. (deprecated)",
    "planning" : "A brewery in planning or not yet opened to the public.",
    "bar" : "A bar. No brewery equipment on premise. (deprecated)",
    "contract" : "A brewery that uses another brewery’s equipment.",
    "proprietor" : "Similar to contract brewing but refers more to a brewery incubator.",
    "closed" : "A location which has been closed."
}

# A few handy JSON types
JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

def http_get(url: str) -> JSONObject:
    response = requests.get(url)
    return response.json()

def condense_query_dict(query_dict: dict[str | int | list]) -> dict[str | int | list]:
    condensed_query_dict = {}
    
    # Removing any keys that don't have any values
    for key, val in query_dict.items():
        if type(val) == list and len(val) == 0:
            continue
        elif val == '':
            continue
        else:
            condensed_query_dict[key] = val.lower()
    
    return condensed_query_dict

def build_obdb_query(query_dict: dict[str | int | list], query_limit: int = 5, query_meta: bool = False) -> str:
    if query_meta:
        url = META_OPEN_BREWERY_DB_URL
    else:
        url = BASE_OPEN_BREWERY_DB_URL
    
    if len(query_dict) == 0:
        return f"{url}?per_page={query_limit}"
    
    query_string = f"{url}?"
    
    for idx, key in enumerate(query_dict):
        # Because of way multiple brewery "type" parameters need to be input we are adding differently and continuing to next param 
        if type(query_dict[key]) == list and len(query_dict[key]) > 0:
            for brew_idx, brewery_type in enumerate(query_dict[key]):
                if idx == 0 and brew_idx == 0:
                    query_string += f"by_{key}={brewery_type}"
                else:
                    query_string += f"&by_{key}={brewery_type}"
            continue
        
        elif type(query_dict[key]) == str:
            param_val = query_dict[key].replace(' ', '_')
        else:
            param_val = query_dict[key]
        
        
        if idx == 0:
            query_string += f"by_{key}={param_val}"
        else:
            query_string += f"&by_{key}={param_val}"
    
    if query_meta:
        return query_string
    else:
        return f"{query_string}&per_page={query_limit}"
    











"""
# Creating functions for each endpoint at Open Brewery DB
# Commenting out queries that don't make sense from user perspective

# def get_single_brewery(obdb_id: str) -> JSONObject:
#     return http_get(f"{BASE_OPEN_BREWERY_DB_URL}/{obdb_id}")


def get_breweries_list(limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?per_page={limit}")


def get_breweries_by_city(city: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_city={city}&per_page={limit}")


def get_breweries_by_country(country: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_city={country.replace(' ', '%20')}&per_page={limit}")


def get_breweries_by_state(state: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_state={state.replace(' ', '%20')}&per_page={limit}")


def get_breweries_by_postal(postal: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_postal={postal}&per_page={limit}")


# def get_breweries_by_distance(lat: float, long: float, limit: int = 3) -> JSONObject:
#     return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_dist={str(lat)},{str(long)}&per_page={limit}")


# def get_breweries_by_ids(id_list: list[str]) -> JSONObject:
#     return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_ids={','.join(id_list)}")


# def get_breweries_by_name(name: str, limit: int = 3) -> JSONObject:
#     return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_ids={'_'.join(name)}&per_page={limit}")


def get_breweries_by_type(brewery_type: str, limit: int = 3) -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}?by_type={brewery_type}&per_page={limit}")


def get_brewery_random() -> JSONObject:
    return http_get(f"{BASE_OPEN_BREWERY_DB_URL}/random")
"""
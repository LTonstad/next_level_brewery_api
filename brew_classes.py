from dataclasses import dataclass
from functools import cached_property
from typing import Optional

import pandas as pd

# Importing static variables and some simple functions
from brew_helpers import *

@dataclass
class OBDBQuery:
    query_string: str
    meta_query_string: str
    query_limit: int
    
    
    @cached_property
    def dataset(self, self.query_string, self.query_limit) - > pd.Dataframe:
        return pd.DataFrame(http_get(obdb_query)).set_index('id')
    
    
@dataclass
class OBDBQueryParams:
    name: Optional[str]
    postal: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    types: Optional[list[str]]
    limit: Optional[int]
    base_url: str = BASE_OPEN_BREWERY_DB_URL
    meta_url: str = META_OPEN_BREWERY_DB_URL
    
    def print_types(self) -> None:
        for brew_type in BREWERY_TYPES:
            print(f"{brew_type}: {BREWERY_TYPES[brew_type]}")
            
    @cached_property
    def query_string(self):
        
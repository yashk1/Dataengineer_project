from urllib import response
import pandas as pd
from pandas import json_normalize
import requests
from collections import namedtuple
import pydantic
from pydantic.dataclasses import dataclass
class Users(pydantic.BaseModel):
    gender: str
    login_uuid: str
    name_title: str
    name_first: str
    name_last: str
    email: str
    dob_date: str
    dob_age: str
    phone: str
    cell: str
    id_name: str = None
    id_value: str
    picture_large: str
    picture_medium: str
    picture_thumbnail: str
    nat: str

    @pydantic.validator('id_value', pre=True, always=True)
    def default_created(cls, id_value):
        return id_value or ''

class Locations(pydantic.BaseModel):
    login_uuid: str
    location_street_number: str
    location_street_name: str
    location_city: str
    location_state: str
    location_country: str
    location_post_code: str = None
    location_coordinates_latitude: str
    location_coordinates_longitude:str
    location_timezone_offset: str
    location_timezone_description: str

    @pydantic.validator('location_post_code', pre=True, always=True)
    def default_created(cls, value):
        return value or ''


class Registration(pydantic.BaseModel):
    login_uuid: str
    login_username: str
    login_password: str
    login_salt: str
    login_md5: str
    login_sha1: str
    login_sha256: str
    registered_date: str
    registered_age: str

table = namedtuple("tablename", "name table columns")
tables = [
    table("Users", Users, ["gender", "email", "phone", "cell", "nat", "name_title", "name_first", "name_last", "login_uuid", "dob_date", "dob_age", "id_name", "id_value", "picture_large", "picture_medium", "picture_thumbnail"]),
    table("Registration", Registration, ["login_uuid", "login_username", "login_password", "login_salt", "login_md5", "login_sha1", "login_sha256", "registered_date", "registered_age"]),
    table("Locations", Locations, ["login_uuid", "location_street_number", "location_street_name", "location_city", "location_state", "location_country", "location_postcode", "location_coordinates_latitude", "location_coordinates_longitude", "location_timezone_offset", "location_timezone_description"])
]


#
def create_csv(name, table, columns, data):
    flattened_data = json_normalize(data, sep='_')
    flattened_data = flattened_data[columns]
    flattened_data = flattened_data.to_dict(orient='records')
    transformed_data = [table(**x).dict() for x in flattened_data]
    transformed_data = pd.DataFrame(transformed_data)

    file_name = "data/" + name + ".csv"

    transformed_data.to_csv(file_name, encoding='utf-8-sig', index=False)

    print(f"{name}.csv created in data")


def iterate_tables(data):
    for t in tables:
        create_csv(t.name, t.table, t.columns, data)

if __name__ == "__main__":
    try:
        url = "https://randomuser.me/api/?results=500"

        #getting the data from above url and storing into "data"
        response = requests.get(url).json()
        data = response["results"]
        iterate_tables(data)
    except:
        print("ERROR: Failed to retrieve data")

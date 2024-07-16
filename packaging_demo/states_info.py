import json
from pathlib import Path
from typing import List

THIS_DIR_PATH = Path(__file__).parent
CITIES_JSON_PATH = THIS_DIR_PATH / "./my_folder/cities.json"


def is_city_capitol_of_state(city_name: str, state: str) -> bool:
    print(CITIES_JSON_PATH)
    cities_json = CITIES_JSON_PATH.read_text()
    cities: List[dict] = json.loads(cities_json)
    matching_cities: List[dict] = [city for city in cities if city["city"] == city_name]
    # print(matching_cities)
    if len(matching_cities) == 0:
        return False
    matching_city_dict = matching_cities[0]
    return matching_city_dict["state"] == state


if __name__ == "__main__":
    print(is_city_capitol_of_state("Juneau", "Alaska"))

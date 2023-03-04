import requests
import json
from constants import ALL_ITEMS_URL, HEADERS

from my_types import CombinationDict


def get_money_making_combinations(
    combinations: list[CombinationDict],
) -> list[CombinationDict]:
    response = requests.get(ALL_ITEMS_URL, headers=HEADERS)
    all_data = json.loads(response.content.decode())["data"]

    combinations_copy = combinations
    for combination in combinations_copy:
        combination["insta_sell_components"] = 0
        combination["insta_buy_components"] = 0
        combination["insta_sell_product"] = 0
        combination["insta_buy_product"] = 0

    for combination in combinations_copy:
        # Components
        components = combination["components"]
        insta_buy_components, insta_sell_components = 0, 0
        for component in components:
            data = all_data[component["id"]]
            insta_buy_components += data["high"] * component["amount"]
            insta_sell_components += data["low"] * component["amount"]
        combination["insta_buy_components"] = insta_buy_components
        combination["insta_sell_components"] = insta_sell_components
        # Product
        data = all_data[combination["product"]]
        combination["insta_buy_product"] = data["high"]
        combination["insta_sell_product"] = data["low"]

    return combinations_copy

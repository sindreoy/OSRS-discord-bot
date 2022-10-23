from typing import TypedDict


class CombinationDict(TypedDict):
    name: str
    components: list[dict[str, str or int]]
    product: str
    insta_sell_components: float
    insta_buy_components: float
    insta_sell_product: float
    insta_buy_product: float

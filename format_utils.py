from my_types import CombinationDict

from tabulate import tabulate


def print_table_of_combinations(combinations: list[CombinationDict]) -> str:
    headers = [
        "Item",
        "Insta buy components",
        "Insta sell components",
        "Insta buy product",
        "Insta sell product",
    ]
    table = [
        (
            [
                combination["name"],
                f"{combination['insta_buy_components']:,.0f}",
                f"{combination['insta_sell_components']:,.0f}",
                f"{combination['insta_buy_product']:,.0f}",
                f"{combination['insta_sell_product']:,.0f}",
            ]
        )
        for combination in combinations
    ]
    return tabulate(table, headers=headers, tablefmt="simple")

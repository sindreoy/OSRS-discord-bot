from my_types import CombinationDict


def print_table_of_combinations(combinations: list[CombinationDict]) -> None:
    len_item_names = [len(item["name"]) for item in combinations]
    max_len = max(len_item_names)
    max_digits = 14
    headers = [
        "Item",
        "Insta buy components",
        "Insta sell components",
        "Insta buy product",
        "Insta sell product",
    ]
    padder = [max_len - len(headers[0]) + max_digits]
    for i in range(1, len(headers)):
        padder.append(len(headers[i]) + 2)
    filler = " "
    text = (
        f"{headers[0]}"
        f"{headers[1] :{filler}>{padder[0]}}"
        f"{headers[2] :{filler}>{padder[1]}}"
        f"{headers[3] :{filler}>{padder[2]}}"
        f"{headers[4] :{filler}>{padder[3]}}"
        "\n"
    )
    for combination in combinations:
        text += (
            f"{combination['name']}"
            f"{combination['insta_buy_components']:>{max_digits},.0f}"
            f"{combination['insta_sell_components']:>{max_digits},.0f}"
            f"{combination['insta_buy_product']:>{max_digits},.0f}"
            f"{combination['insta_sell_product']:>{max_digits},.0f}"
            "\n"
        )
    return text

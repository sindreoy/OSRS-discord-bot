SCHEME = "https://"
BASE_URL = SCHEME + "prices.runescape.wiki/api/v1/osrs"
ALL_ITEMS_URL = BASE_URL + "/latest"
ITEMS_URL = ALL_ITEMS_URL + "?id="

HEADERS = {
    "User-Agent": "Combine items tracker - @sindreoy#9154",
    "From": "sindre.bakke.oyen@gmail.com",  # This is another valid field
}

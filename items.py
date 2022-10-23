from my_types import CombinationDict

LIST_OF_COMBINATIONS: list[CombinationDict] = [
    # Godsword blade
    {
        "name": "Godsword blade",
        "components": [
            {"id": "11818", "amount": 1},  # shard 1
            {"id": "11820", "amount": 1},  # shard 2
            {"id": "11822", "amount": 1},  # shard 3
        ],
        "product": "11798",  # Godsword blade
    },
    # BoFa from seed
    {
        "name": "BoFa from seed",
        "components": [
            {"id": "25859", "amount": 1},  # enh.cryst.wep.seed
            {"id": "23959", "amount": 2 / 3},  # crystal shards
        ],
        "product": "25862",  # BoFa
    },
    # BoFa from Blade
    {
        "name": "BoFa from Blade",
        "components": [
            {"id": "23997", "amount": 1},  # Blade
            {"id": "23959", "amount": 7 / 3},  # crystal shards
        ],
        "product": "25862",  # BoFa
    },
    # Smash BoFa to seed
    {
        "name": "Blade to seed",
        "components": [
            {"id": "25862", "amount": 1},  # BoFa
            {"id": "23959", "amount": 5 / 3},  # crystal shards
        ],
        "product": "25859",  # enh.cryst.wep.seed
    },
    # Smash Blade to seed
    {
        "name": "BoFa to seed",
        "components": [
            {"id": "25862", "amount": 1},  # BoFa
            {"id": "23959", "amount": 5 / 3},  # crystal shards
        ],
        "product": "25859",  # enh.cryst.wep.seed
    },
    # Barrows items
    # Dharok
    {
        "name": "Dharok set",
        "components": [
            {"id": "4718", "amount": 1},  # weapon
            {"id": "4716", "amount": 1},  # helm
            {"id": "4720", "amount": 1},  # body
            {"id": "4722", "amount": 1},  # legs
        ],
        "product": "12877",  # Dharok set
    },
    # Karil
    {
        "name": "Karil set",
        "components": [
            {"id": "4732", "amount": 1},  # weapon
            {"id": "4734", "amount": 1},  # helm
            {"id": "4738", "amount": 1},  # body
            {"id": "4736", "amount": 1},  # legs
        ],
        "product": "12883",  # Karil set
    },
    # Guthan
    {
        "name": "Guthan set",
        "components": [
            {"id": "4726", "amount": 1},  # weapon
            {"id": "4724", "amount": 1},  # helm
            {"id": "4728", "amount": 1},  # body
            {"id": "4730", "amount": 1},  # legs
        ],
        "product": "12873",  # Guthan set
    },
    # Ahrim
    {
        "name": "Ahrim set",
        "components": [
            {"id": "4710", "amount": 1},  # weapon
            {"id": "4708", "amount": 1},  # helm
            {"id": "4712", "amount": 1},  # body
            {"id": "4714", "amount": 1},  # legs
        ],
        "product": "12881",  # Ahrim set
    },
    # Verac
    {
        "name": "Verac set",
        "components": [
            {"id": "4755", "amount": 1},  # weapon
            {"id": "4753", "amount": 1},  # helm
            {"id": "4757", "amount": 1},  # body
            {"id": "4759", "amount": 1},  # legs
        ],
        "product": "12875",  # Verac set
    },
    # Inquisitor
    {
        "name": "Inquisitor set",
        "components": [
            {"id": "24419", "amount": 1},  # helm
            {"id": "24420", "amount": 1},  # body
            {"id": "24421", "amount": 1},  # legs
        ],
        "product": "24488",  # Inquisitor set
    },
    # Zaryte crossbow
    {
        "name": "Zaryte crossbow",
        "components": [
            {"id": "26372", "amount": 1},  # Nihil horn
            {"id": "11785", "amount": 1},  # ACB
        ],
        "product": "26374",  # Zaryte crossbow
    },
    # Dismantle Arcane
    {
        "name": "Arcane sigil",
        "components": [{"id": "12825", "amount": 1}],
        "product": "12827",
    },
    # Masori set
    {
        "name": "Masori armor set (f)",
        "components": [
            {"id": "27235", "amount": 1},  # helm
            {"id": "27238", "amount": 1},  # body
            {"id": "27241", "amount": 1},  # legs
        ],
        "product": "27355",
    },
    # Masori mask to fortified
    {
        "name": "Masori mask to fortified",
        "components": [
            {"id": "27226", "amount": 1},  # masori helm
            {"id": "11826", "amount": 1},  # arma helm
        ],
        "product": "27235",  # Masori helm (f)
    },
    # Masori body to fortified
    {
        "name": "Masori body to fortified",
        "components": [
            {"id": "27229", "amount": 1},  # masori body
            {"id": "11828", "amount": 1},  # arma chest
        ],
        "product": "27238",  # Masori body (f)
    },
    # Masori chaps to fortified
    {
        "name": "Masori chaps to fortified",
        "components": [
            {"id": "27232", "amount": 1},  # masori legs
            {"id": "11830", "amount": 1},  # arma legs
        ],
        "product": "27241",  # Masori chaps (f)
    },
]

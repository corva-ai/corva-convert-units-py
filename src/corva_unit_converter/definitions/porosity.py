metric = {
    # ratio from 0 - 1
    "v/v": {
        "name": {
            "singular": "v/v",
            "plural": "v/v",
            "display": "v/v"
        },
        "to_anchor": 100,
        "aliases": [
            "v/v"
        ]
    },
    # A percentage 0 - 100%
    "pu": {
        "name": {
            "singular": "pu",
            "plural": "pu",
            "display": "pu"
        },
        "to_anchor": 1,
        "aliases": [
            "pu"
        ]
    }
}

imperial = {
    "pu": {
        "name": {
            "singular": "pu",
            "plural": "pu",
            "display": "pu"
        },
        "to_anchor": 1,
        "aliases": [
            "pu"
        ]
    }
}

rule = {
    "metric": metric,
    "imperial": imperial,
    "_anchors": {
        "metric": {
            "unit": "pu",
            "ratio": 1
        },
        "imperial": {
            "unit": "pu",
            "ratio": 1
        }
    }
}

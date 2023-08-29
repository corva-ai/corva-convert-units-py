metric = {
    "Units (0-10000u)": {
        "name": {
            "singular": "Unit (0-10000u)",
            "plural": "Units (0-10000u)",
            "display": "Units (0-10000u)"
        },
        "to_anchor": 1 / 100,
        "aliases": [
            "Units (0-10000u)"
        ]
    },
    "Units (0-5000u)": {
        "name": {
            "singular": "Unit (0-5000u)",
            "plural": "Units (0-5000u)",
            "display": "Units (0-5000u)"
        },
        "to_anchor": 1 / 50,
        "aliases": [
            "Units (0-5000u)"
        ]
    },
    # An alias for Unit (0-5000) added for international customers
    "Units": {
        "name": {
            "singular": "Unit",
            "plural": "Units",
            "display": "Units"
        },
        "to_anchor": 1 / 50,
        "aliases": [
            "Units"
        ]
    },
    "%EMA": {
        "name": {
            "singular": "%EMA",
            "plural": "%EMA",
            "display": "%EMA"
        },
        "to_anchor": 1,
        "aliases": [
            "%EMA"
        ]
    },
    "%": {
        "name": {
            "singular": "%",
            "plural": "%",
            "display": "%"
        },
        "to_anchor": 1,
        "aliases": [
            "%"
        ]
    },
    "ppm": {
        "name": {
            "singular": "ppm",
            "plural": "ppm",
            "display": "ppm"
        },
        "to_anchor": 1 / 10000,
        "aliases": [
            "ppm"
        ]
    }
}

rule = {
    "metric": metric,
    "imperial": metric,
    "_anchors": {
        "metric": {
            "unit": "%EMA",
            "ratio": 1
        },
        "imperial": {
            "unit": "%EMA",
            "ratio": 1
        }
    }
}

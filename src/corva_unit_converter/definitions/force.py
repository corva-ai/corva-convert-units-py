metric = {
    "N": {
        "name": {
            "singular": "Newton",
            "plural": "Newtons",
            "display": "N"
        },
        "to_anchor": 1,
        "aliases": [
            "N"
        ]
    },
    "daN": {
        "name": {
            "singular": "Dekanewton",
            "plural": "Dekanewtons",
            "display": "daN"
        },
        "to_anchor": 10,
        "aliases": [
            "daN"
        ]
    },
    "kdaN": {
        "name": {
            "singular": "KiloDekanewton",
            "plural": "KiloDekanewtons",
            "display": "kdaN"
        },
        "to_anchor": 10000,
        "aliases": [
            "kdaN"
        ]
    }
}

imperial = {
    "lbf": {
        "name": {
            "singular": "Pound Force",
            "plural": "Pound Force",
            "display": "lbf"
        },
        "to_anchor": 1,
        "aliases": [
            "lbf"
        ]
    },
    "klbf": {
        "name": {
            "singular": "Kilopound Force",
            "plural": "Kilopound Force",
            "display": "klbf"
        },
        "to_anchor": 1000,
        "aliases": [
            "klbf"
        ]
    }
}

rule = {
    "metric": metric,
    "imperial": imperial,
    "_anchors": {
        "metric": {
            "unit": "N",
            "ratio": 0.2248089431
        },
        "imperial": {
            "unit": "lbf",
            "ratio": 1 / 0.2248089431
        }
    }
}

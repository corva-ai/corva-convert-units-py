from ..constants import g

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
    "kN": {
        "name": {
            "singular": "Kilonewton",
            "plural": "Kilonewtons",
            "display": "kN"
        },
        "to_anchor": 1000,
        "aliases": [
            "kN"
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
    },
    "TONNEf": {
        "name": {
            "singular": "Ton Force (metric)",
            "plural": "Ton Force (metric)",
            "display": "TONNEf"
        },
        "to_anchor": 1000 * g,
        "aliases": [
            "TONNEf"
        ]
    },
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
    },
    "TONf US": {
        "name": {
            "singular": "Ton Force (short)",
            "plural": "Ton Force (short)",
            "display": "TONf US"
        },
        "to_anchor": 2000,
        "aliases": [
            "TONf US"
        ]
    },
    "TONf(long)": {
        "name": {
            "singular": "Ton Force (long)",
            "plural": "Ton Force (long)",
            "display": "TONf(long)"
        },
        "to_anchor": 2240,
        "aliases": [
            "TONf(long)"
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

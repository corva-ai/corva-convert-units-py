metric = {
    "Pa": {
        "name": {
            "singular": "pascal",
            "plural": "pascals",
            "display": "Pa"
        },
        "to_anchor": 1 / 1000,
        "aliases": [
            "Pa"
        ]
    },
    "kPa": {
        "name": {
            "singular": "kilopascal",
            "plural": "kilopascals",
            "display": "kPa"
        },
        "to_anchor": 1,
        "aliases": [
            "kPa"
        ]
    },
    "kPaAdjusted": {
        "name": {
            "singular": "kilopascal adjusted",
            "plural": "kilopascals adjusted",
            "display": "adjusted kPa"
        },
        "to_anchor": 0.35,
        "aliases": [
            "kPaadjusted"
        ]
    },
    "MPa": {
        "name": {
            "singular": "megapascal",
            "plural": "megapascals",
            "display": "MPa"
        },
        "to_anchor": 1000,
        "aliases": [
            "MPa"
        ]
    },
    "hPa": {
        "name": {
            "singular": "hectopascal",
            "plural": "hectopascals",
            "display": "hPa"
        },
        "to_anchor": 1 / 10,
        "aliases": [
            "hPa"
        ]
    },
    "bar": {
        "name": {
            "singular": "bar",
            "plural": "bar",
            "display": "bar"
        },
        "to_anchor": 100,
        "aliases": [
            "bar"
        ]
    },
    "torr": {
        "name": {
            "singular": "torr",
            "plural": "torr",
            "display": "torr"
        },
        "to_anchor": 101325 / 760000,
        "aliases": [
            "torr"
        ]
    }
}

imperial = {
    "psi": {
        "name": {
            "singular": "pound per square inch",
            "plural": "pounds per square inch",
            "display": "psi"
        },
        "to_anchor": 1 / 1000,
        "aliases": [
            "psi"
        ]
    },
    "psiAdjusted": {
        "name": {
            "singular": "adjusted pound per square inch",
            "plural": "adjusted pounds per square inch",
            "display": "adjusted psi"
        },
        "to_anchor": (1 / 1000) * 0.35,
        "aliases": [
            "psiAdjusted"
        ]
    },
    "ksi": {
        "name": {
            "singular": "kilopound per square inch",
            "plural": "kilopounds per square inch",
            "display": "ksi"
        },
        "to_anchor": 1,
        "aliases": [
            "ksi"
        ]
    },
    "ksiAdjusted": {
        "name": {
            "singular": "adjusted kilopound per square inch",
            "plural": "adjusted kilopounds per square inch",
            "display": "adjusted ksi"
        },
        "to_anchor": 0.35,
        "aliases": [
            "ksiAdjusted"
        ]
    },
    "psf": {
        "name": {
            "singular": "pound per square foot",
            "plural": "pounds per square foot",
            "display": "lbf/ft²"
        },
        "to_anchor": (1 / 144) / 1000,
        "aliases": [
            "psf"
        ]
    },
    "dsf": {
        "name": {
            "singular": "decapound per square foot",
            "plural": "pound per deca square foot",
            "display": "lbf/(10·ft²)"
        },
        "to_anchor": ((1 / 144) / 10000),
        "aliases": [
            "dsf"
        ]
    },
    "hsf": {
        "name": {
            "singular": "hectopound per square foot",
            "plural": "pound per hecto square foot",
            "display": "lbf/(100·ft²)"
        },
        "to_anchor": ((1 / 144) / 100000),
        "aliases": [
            "hsf"
        ]
    }
}

rule = {
    "metric": metric,
    "imperial": imperial,
    "_anchors": {
        "metric": {
            "unit": "kPa",
            "ratio": 0.00014503768078
        },
        "imperial": {
            "unit": "ksi",
            "ratio": 1 / 0.00014503768078
        }
    }
}

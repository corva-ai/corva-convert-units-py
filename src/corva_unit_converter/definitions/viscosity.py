metric = {
    "mpas": {
        "name": {
            "singular": "Millipascal-second",
            "plural": "Millipascal-seconds",
            "display": "mPa·s",
        },
        "to_anchor": 1,
        "aliases": ["cP", "mPa·s", "mPa.s", "mPa*s"],
    },
    "pas": {
        "name": {
            "singular": "Pascal-second",
            "plural": "Pascal-seconds",
            "display": "Pa·s",
        },
        "to_anchor": 1000,
        "aliases": ["Pa·s", "Pa.s", "Pa*s"],
    },
}

rule = {
    "metric": metric,
    "_anchors": {
        "metric": {
            "unit": "s",
            "ratio": 1
        }
    }
}

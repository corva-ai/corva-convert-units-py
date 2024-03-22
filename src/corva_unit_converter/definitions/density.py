# Specific gravity is the ratio of a material's density with that of water at 4 °C
# (where it is most dense and is taken to have the value 999.974 kg m-3)
# Used as 1 here
metric = {
    "Sg": {
        "name": {
            "singular": "Specific Gravity",
            "plural": "Specific Gravity",
            "display": "Sg"
        },
        "to_anchor": 1,
        "aliases": [
            "Sg"
        ]
    },
    "kg/m3": {
        "name": {
            "singular": "Kilogram per Cubic Meter",
            "plural": "Kilograms per Cubic Meter",
            "display": "kg/m³"
        },
        "to_anchor": 1 / 1000,
        "aliases": [
            "kg/m3"
        ]
    },
    "kg/cm3": {
        "name": {
            "singular": "Kilogram per Cubic Centimeter",
            "plural": "Kilograms per Cubic Centimeter",
            "display": "kg/cm³"
        },
        "to_anchor": 1000,
        "aliases": [
            "kg/cm3"
        ]
    },
    "g/cm3": {
        "name": {
            "singular": "Gram per Cubic Centimeter",
            "plural": "Grams per Cubic Centimeter",
            "display": "g/cm³"
        },
        "to_anchor": 1,
        "aliases": [
            "g/c3",
            "g/cc",
            "g/cm3"
        ]
    },
    "g/l": {
        "name": {
            "singular": "Gram per Liter",
            "plural": "Grams per Liter",
            "display": "g/l"
        },
        "to_anchor": 1 / 1000,
        "aliases": [
            "g/l"
        ]
    },
    "g/m3": {
        "name": {
            "singular": "Gram per Cubic Meter",
            "plural": "Grams per Cubic Meter",
            "display": "g/m3"
        },
        "to_anchor": 1 / 1000000,
        "aliases": [
            "gm/3",
            "gm/c"
        ]
    }
}

imperial = {
    "lb/gal": {  # lb/gal is used for mass concentration
        "name": {
            "singular": "Pound Per Gallon",
            "plural": "Pounds Per Gallon",
            "display": "lb/gal"
        },
        "to_anchor": 1,
        "aliases": [
            "lb/gal"
        ]
    },
    # https://glossary.slb.com/en/terms/p/ppg
    # lbm/galUS
    # Abbreviation for density, pounds per gallon, more correctly written lbm/galUS.
    # For example, the density of water is 8.33 ppg at 60 degF [16 degC].
    # The "US" is included to differentiate between US gallons and UK gallons.
    "ppg": {
        "name": {
            "singular": "Pound Per Gallon",
            "plural": "Pounds Per Gallon",
            "display": "ppg"
        },
        "to_anchor": 1,
        "aliases": [
            "ppg"
        ]
    },
    "lb/Mgal": {
        "name": {
            "singular": "Pound per 1000 Gallon",
            "plural": "Pounds per 1000 Gallon",
            "display": "lb/Mgal"
        },
        "to_anchor": 1 / 1000,
        "aliases": [
            "lb/Mgal"
        ]
    },
    "lb/ft3": {
        "name": {
            "singular": "Pound per Cubic Foot",
            "plural": "Pounds per Cubic Foot",
            "display": "lb/ft³"
        },
        # Gallon in liters / Cubic Foot in liters
        "to_anchor": 3.785411784 / 28.316846592,
        "aliases": [
            "lb/ft3"
        ]
    },
    "lb/in3": {
        "name": {
            "singular": "Pound per Cubic Inch",
            "plural": "Pounds per Cubic Inch",
            "display": "lb/in³"
        },
        # Gallon in liters / Cubic inch in liters
        "to_anchor": 3.785411784 / 0.0163870640,
        "aliases": [
            "lb/in3"
        ]
    }
}

rule = {
    "metric": metric,
    "imperial": imperial,
    "_anchors": {
        "metric": {
            "unit": "Sg",
            "ratio": 1 / 0.1198264
        },
        "imperial": {
            "unit": "ppg",
            "ratio": 0.1198264
        }
    }
}

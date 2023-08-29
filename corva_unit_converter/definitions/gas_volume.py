metric = {
    "mm3": {
        "name": {
            "singular": "Cubic Millimeter",
            "plural": "Cubic Millimeters",
            "display": "mm³"
        },
        "to_anchor": 1 / 1000000000
    },
    "cm3": {
        "name": {
            "singular": "Cubic Centimeter",
            "plural": "Cubic Centimeters",
            "display": "cm³"
        },
        "to_anchor": 1 / 1000000
    },
    "ml": {
        "name": {
            "singular": "Millilitre",
            "plural": "Millilitres",
            "display": "ml"
        },
        "to_anchor": 1 / 1000000
    },
    "cl": {
        "name": {
            "singular": "Centilitre",
            "plural": "Centilitres",
            "display": "cl"
        },
        "to_anchor": 1 / 100000
    },
    "dl": {
        "name": {
            "singular": "Decilitre",
            "plural": "Decilitres",
            "display": "dl"
        },
        "to_anchor": 1 / 10000
    },
    "l": {
        "name": {
            "singular": "Litre",
            "plural": "Litres",
            "display": "l"
        },
        "to_anchor": 1 / 1000
    },
    "m3": {
        "name": {
            "singular": "Cubic meter",
            "plural": "Cubic meters",
            "display": "m³"
        },
        "to_anchor": 1
    },
    "km3": {
        "name": {
            "singular": "Cubic kilometer",
            "plural": "Cubic kilometers",
            "display": "km³"
        },
        "to_anchor": 1000000000
    },
    # Swedish units
    "krm": {
        "name": {
            "singular": "Matsked",
            "plural": "Matskedar",
            "display": "krm"
        },
        "to_anchor": 1 / 1000000
    },
    "tsk": {
        "name": {
            "singular": "Tesked",
            "plural": "Teskedar",
            "display": "tsk"
        },
        "to_anchor": 5 / 1000000
    },
    "msk": {
        "name": {
            "singular": "Matsked",
            "plural": "Matskedar",
            "display": "msk"
        },
        "to_anchor": 15 / 1000000
    },
    "kkp": {
        "name": {
            "singular": "Kaffekopp",
            "plural": "Kaffekoppar",
            "display": "kkp"
        },
        "to_anchor": 150 / 1000000
    },
    "glas": {
        "name": {
            "singular": "Glas",
            "plural": "Glas",
            "display": "glas"
        },
        "to_anchor": 200 / 1000000
    },
    "kanna": {
        "name": {
            "singular": "Kanna",
            "plural": "Kannor",
            "display": "kanna"
        },
        "to_anchor": 2.617 / 1000
    }
}

imperial = {
    "tsp": {
        "name": {
            "singular": "Teaspoon",
            "plural": "Teaspoons",
            "display": "tsp"
        },
        "to_anchor": 0.000000174
    },
    "Tbs": {
        "name": {
            "singular": "Tablespoon",
            "plural": "Tablespoons",
            "display": "tbsp"
        },
        "to_anchor": 0.000000522
    },
    "in3": {
        "name": {
            "singular": "Cubic inch",
            "plural": "Cubic inches",
            "display": "in³"
        },
        "to_anchor": 0.000000579
    },
    "fl-oz": {
        "name": {
            "singular": "Fluid Ounce",
            "plural": "Fluid Ounces",
            "display": "fl-oz"
        },
        "to_anchor": 0.00000104
    },
    "cup": {
        "name": {
            "singular": "Cup",
            "plural": "Cups",
            "display": "cup"
        },
        "to_anchor": 0.00000835
    },
    "pnt": {
        "name": {
            "singular": "Pint",
            "plural": "Pints",
            "display": "pint"
        },
        "to_anchor": 0.0000167
    },
    "qt": {
        "name": {
            "singular": "Quart",
            "plural": "Quarts",
            "display": "qt"
        },
        "to_anchor": 0.0000334
    },
    "gal": {
        "name": {
            "singular": "Gallon",
            "plural": "Gallons",
            "display": "gal"
        },
        "to_anchor": 0.000133
    },
    "ft3": {
        "name": {
            "singular": "Cubic foot",
            "plural": "Cubic feet",
            "display": "ft³"
        },
        "to_anchor": 1000
    },
    "yd3": {
        "name": {
            "singular": "Cubic yard",
            "plural": "Cubic yards",
            "display": "yd³"
        },
        "to_anchor": 0.0269
    },
    "bbl": {
        "name": {
            "singular": "Oil barrel",
            "plural": "Oil barrels",
            "display": "bbl"
        },
        "to_anchor": 0.0056
    },
    "Mscf": {
        "name": {
            "singular": "Thousand standard cubic foot",
            "plural": "Thousand standard cubic feet",
            "display": "Mscf"
        },
        "to_anchor": 1
    }
}

rule = {
    "metric": metric,
    "imperial": imperial,
    "_anchors": {
        "metric": {
            "unit": "m3",
            "ratio": 0.0353
        },
        "imperial": {
            "unit": "Mscf",
            "ratio": 1 / 0.0353
        }
    }
}

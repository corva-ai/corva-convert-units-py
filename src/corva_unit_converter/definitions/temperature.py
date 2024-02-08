metric = {
   "C": {
      "name": {
         "singular": "degree Celsius",
         "plural": "degrees Celsius",
         "display": "°C"
      },
      "to_anchor": 1,
      "anchor_shift": 0,
      "aliases": [
         "degc"
      ]
   },
   "K": {
      "name": {
         "singular": "degree Kelvin",
         "plural": "degrees Kelvin",
         "display": "°K"
      },
      "to_anchor": 1,
      "anchor_shift": 273.15,
      "aliases": [
         "degk"
      ]
   }
}

imperial = {
   "F": {
      "name": {
         "singular": "degree Fahrenheit",
         "plural": "degrees Fahrenheit",
         "display": "°F"
      },
      "to_anchor": 1,
      "aliases": [
         "degf"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "C",
         "transform": lambda c: c / (5 / 9) + 32,
         "ratio": 1
      },
      "imperial": {
         "unit": "F",
         "transform": lambda f: (f - 32) * (5 / 9),
         "ratio": 1
      }
   }
}

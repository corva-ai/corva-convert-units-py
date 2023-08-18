current = {
   "A": {
      "name": {
         "singular": "Ampere",
         "plural": "Amperes",
         "display": "A"
      },
      "to_anchor": 1000,
      "aliases": [
         "A"
      ]
   },
   "mA": {
      "name": {
         "singular": "Milliampere",
         "plural": "Milliamperes",
         "display": "mA"
      },
      "to_anchor": 1,
      "aliases": [
         "mA"
      ]
   }
}

rule = {
   "metric": current,
   "imperial": current,
   "_anchors": {
      "metric": {
         "unit": "mA",
         "ratio": 1
      },
      "imperial": {
         "unit": "mA",
         "ratio": 1
      }
   }
}

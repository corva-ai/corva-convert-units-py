metric = {
   "mhp": {
      "name": {
         "singular": "metric horsepower",
         "plural": "metric horsepower",
         "display": "mhp"
      },
      "to_anchor": 1,
      "aliases": [
         "mhp"
      ]
   },
   "watt": {
      "name": {
         "singular": "watt",
         "plural": "watts",
         "display": "W"
      },
      "to_anchor": 1/735.499,
      "aliases": [
         "watt"
      ]
   }
}

imperial = {
   "hp": {
      "name": {
         "singular": "horsepower",
         "plural": "horsepower",
         "display": "hp"
      },
      "to_anchor": 1,
      "aliases": [
         "hp"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "mhp",
         "ratio": 0.9863
      },
      "imperial": {
         "unit": "hp",
         "ratio": 1 / 0.9863
      }
   }
}

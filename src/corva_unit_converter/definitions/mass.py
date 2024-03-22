metric = {
   "mcg": {
      "name": {
         "singular": "Microgram",
         "plural": "Micrograms",
         "display": "mcg"
      },
      "to_anchor": 1 / 1000000,
      "aliases": [
         "mcg"
      ]
   },
   "mg": {
      "name": {
         "singular": "Milligram",
         "plural": "Milligrams",
         "display": "mg"
      },
      "to_anchor": 1 / 1000,
      "aliases": [
         "mg"
      ]
   },
   "g": {
      "name": {
         "singular": "Gram",
         "plural": "Grams",
         "display": "g"
      },
      "to_anchor": 1,
      "aliases": [
         "g"
      ]
   },
   "kg": {
      "name": {
         "singular": "Kilogram",
         "plural": "Kilograms",
         "display": "kg"
      },
      "to_anchor": 1000,
      "aliases": [
         "kg"
      ]
   },
   "ton": {
      "name": {
         "singular": "Ton",
         "plural": "Tons",
         "display": "t"
      },
      "to_anchor": 1000 * 1000,
      "aliases": [
         "ton"
      ]
   }
}

imperial = {
   "oz": {
      "name": {
         "singular": "Ounce",
         "plural": "Ounces",
         "display": "oz"
      },
      "to_anchor": 1 / 16,
      "aliases": [
         "oz"
      ]
   },
   "lb": {
      "name": {
         "singular": "Pound",
         "plural": "Pounds",
         "display": "lb"
      },
      "to_anchor": 1,
      "aliases": [
         "lb"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "g",
         "ratio": 1 / 453.592
      },
      "imperial": {
         "unit": "lb",
         "ratio": 453.592
      }
   }
}

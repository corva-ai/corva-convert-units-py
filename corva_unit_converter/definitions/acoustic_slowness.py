metric = {
   "us/m": {
      "name": {
         "singular": "us/m",
         "plural": "us/m",
         "display": "us/m"
      },
      "to_anchor": 1,
      "aliases": [
         "us/m"
      ]
   }
}

imperial = {
   "us/ft": {
      "name": {
         "singular": "us/ft",
         "plural": "us/ft",
         "display": "us/ft"
      },
      "to_anchor": 1,
      "aliases": [
         "us/f",
         "us/ft"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "us/m",
         "ratio": 1 / 3.28084
      },
      "imperial": {
         "unit": "us/ft",
         "ratio": 3.28084
      }
   }
}

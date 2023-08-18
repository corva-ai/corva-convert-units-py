metric = {
   "kPa/m": {
      "name": {
         "singular": "kilopascal per meter",
         "plural": "kilopascals per meter",
         "display": "kPa/m"
      },
      "to_anchor": 1,
      "aliases": [
         "kPa/m"
      ]
   }
}

imperial = {
   "psi/ft": {
      "name": {
         "singular": "pressure per unit",
         "plural": "pressure per unit",
         "display": "psi/ft"
      },
      "to_anchor": 1,
      "aliases": [
         "psi/ft"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "kPa/m",
         "ratio": 0.0442075
      },
      "imperial": {
         "unit": "psi/ft",
         "ratio": 1 / 0.0442075
      }
   }
}

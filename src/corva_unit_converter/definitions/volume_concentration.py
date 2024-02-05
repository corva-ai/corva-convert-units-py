metric = {
   "l/m3": {
      "name": {
         "singular": "Liter per Cubic Meter",
         "plural": "Liters per Cubic Meter",
         "display": "l/m3"
      },
      "to_anchor": 1,
      "aliases": [
         "l/m3"
      ]
   }
}

imperial = {
   "gal/Mgal": {
      "name": {
         "singular": "Gallon per 1000 Gallon",
         "plural": "Gallons per 1000 Gallon",
         "display": "gal/Mgal"
      },
      "to_anchor": 1,
      "aliases": [
         "gal/Mgal"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "l/m3",
         "ratio": 1
      },
      "imperial": {
         "unit": "gal/Mgal",
         "ratio": 1
      }
   }
}

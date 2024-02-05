metric = {
   "mm/rev": {
      "name": {
         "singular": "Millimeter per Revolution",
         "plural": "Millimeters per Revolution",
         "display": "mm/rev"
      },
      "to_anchor": 1,
      "aliases": [
         "mm/rev"
      ]
   },
   "m/rev": {
      "name": {
         "singular": "Meter per Revolution",
         "plural": "Meters per Revolution",
         "display": "m/rev"
      },
      "to_anchor": 1000,
      "aliases": [
         "m/rev"
      ]
   }
}

imperial = {
   "in/rev": {
      "name": {
         "singular": "Inch per Revolution",
         "plural": "Inches per Revolution",
         "display": "in/rev"
      },
      "to_anchor": 1,
      "aliases": [
         "in/rev"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "mm/rev",
         "ratio": 1/25.4
      },
      "imperial": {
         "unit": "in/rev",
         "ratio": 25.4
      }
   }
}

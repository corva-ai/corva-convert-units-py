# Mass-per-length
metric = {
   "kg-m": {
      "name": {
         "singular": "Kilogram per Meter",
         "plural": "Kilograms per Meter",
         "display": "kg/m"
      },
      "to_anchor": 1,
      "aliases": [
         "kg-m"
      ]
   }
}

imperial = {
   "lb-ft": {
      "name": {
         "singular": "Pound per Foot",
         "plural": "Pounds per Foot",
         "display": "lb/ft"
      },
      "to_anchor": 1,
      "aliases": [
         "lb-ft"
      ]
   },
   "klb-ft": {
      "name": {
         "singular": "Kilopound per Foot",
         "plural": "Kilopounds per Foot",
         "display": "klb/ft"
      },
      "to_anchor": 1000,
      "aliases": [
         "klb-ft"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "kg-m",
         "ratio": 1 / 1.48816
      },
      "imperial": {
         "unit": "lb-ft",
         "ratio": 1.48816
      }
   }
}

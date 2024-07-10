voltage = {
   "V": {
      "name": {
         "singular": "Volt",
         "plural": "Volts",
         "display": "V"
      },
      "to_anchor": 1000,
      "aliases": [
         "V"
      ]
   },
   "mV": {
      "name": {
         "singular": "Millivolt",
         "plural": "Millivolts",
         "display": "mV"
      },
      "to_anchor": 1,
      "aliases": [
         "mV"
      ]
   },
   "nV": {
      "name": {
         "singular": "Nanovolt",
         "plural": "Nanovolts",
         "display": "nV"
      },
      "to_anchor": 1/1000000,
      "aliases": [
         "nV"
      ]
   }
}

rule = {
   "metric": voltage,
   "imperial": voltage,
   "_anchors": {
      "metric": {
         "unit": "mV",
         "ratio": 1
      },
      "imperial": {
         "unit": "mV",
         "ratio": 1
      }
   }
}

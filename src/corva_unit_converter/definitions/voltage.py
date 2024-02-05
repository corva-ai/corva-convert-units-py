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

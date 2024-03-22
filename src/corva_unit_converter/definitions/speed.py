metric = {
   "m/s": {
      "name": {
         "singular": "Meter per second",
         "plural": "Meters per second",
         "display": "m/s"
      },
      "to_anchor": 3.6,
      "aliases": [
         "m/s"
      ]
   },
   "m/min": {
      "name": {
         "singular": "Meter per minute",
         "plural": "Meters per minute",
         "display": "m/min"
      },
      "to_anchor": 0.06,
      "aliases": [
         "m/min"
      ]
   },
   "m/h": {
      "name": {
         "singular": "Meter per hour",
         "plural": "Meters per hour",
         "display": "m/h"
      },
      "to_anchor": 1 / 1000,
      "aliases": [
         "m/h"
      ]
   },
   "kph": {
      "name": {
         "singular": "Kilometer per hour",
         "plural": "Kilometers per hour",
         "display": "kph"
      },
      "to_anchor": 1,
      "aliases": [
         "kph"
      ]
   }
}

imperial = {
   "mph": {
      "name": {
         "singular": "Mile per hour",
         "plural": "Miles per hour",
         "display": "mph"
      },
      "to_anchor": 1,
      "aliases": [
         "mph"
      ]
   },
   "knot": {
      "name": {
         "singular": "Knot",
         "plural": "Knots",
         "display": "knot"
      },
      "to_anchor": 1.150779,
      "aliases": [
         "knot"
      ]
   },
   "ft/s": {
      "name": {
         "singular": "Foot per second",
         "plural": "Feet per second",
         "display": "ft/s"
      },
      "to_anchor": 0.681818,
      "aliases": [
         "ft/s"
      ]
   },
   "ft/min": {
      "name": {
         "singular": "Foot per minute",
         "plural": "Feet per minute",
         "display": "ft/min"
      },
      "to_anchor": 0.0113636,
      "aliases": [
         "ft/min"
      ]
   },
   "ft/h": {
      "name": {
         "singular": "Foot per hour",
         "plural": "Feet per hour",
         "display": "ft/h"
      },
      "to_anchor": 1 / 5280,
      "aliases": [
         "ft/h"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "kph",
         "ratio": 1 / 1.609344
      },
      "imperial": {
         "unit": "mph",
         "ratio": 1.609344
      }
   }
}

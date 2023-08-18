metric = {
   "mcg/s": {
      "name": {
         "singular": "Microgram per second",
         "plural": "Micrograms per second",
         "display": "mcg/s"
      },
      "to_anchor": 1 / 1000000,
      "aliases": [
         "mcg/s"
      ]
   },
   "mcg/min": {
      "name": {
         "singular": "Microgram per minute",
         "plural": "Micrograms per minute",
         "display": "mcg/min"
      },
      "to_anchor": 1 / (1000000 * 60),
      "aliases": [
         "mcg/min"
      ]
   },
   "mcg/h": {
      "name": {
         "singular": "Microgram per hour",
         "plural": "Micrograms per hour",
         "display": "mcg/h"
      },
      "to_anchor": 1 / (1000000 * 3600),
      "aliases": [
         "mcg/h"
      ]
   },
   "mg/s": {
      "name": {
         "singular": "Milligram per second",
         "plural": "Milligrams per second",
         "display": "mg/s"
      },
      "to_anchor": 1 / 1000,
      "aliases": [
         "mg/s"
      ]
   },
   "mg/min": {
      "name": {
         "singular": "Milligram per minute",
         "plural": "Milligrams per minute",
         "display": "mg/min"
      },
      "to_anchor": 1 / (1000 * 60),
      "aliases": [
         "mg/min"
      ]
   },
   "mg/h": {
      "name": {
         "singular": "Milligram per hour",
         "plural": "Milligrams per hour",
         "display": "mg/h"
      },
      "to_anchor": 1 / (1000 * 3600),
      "aliases": [
         "mg/h"
      ]
   },
   "g/s": {
      "name": {
         "singular": "Gram per second",
         "plural": "Grams per second",
         "display": "g/s"
      },
      "to_anchor": 1,
      "aliases": [
         "g/s"
      ]
   },
   "g/min": {
      "name": {
         "singular": "Gram per minute",
         "plural": "Grams per minute",
         "display": "g/min"
      },
      "to_anchor": 1 / 60,
      "aliases": [
         "g/min"
      ]
   },
   "g/h": {
      "name": {
         "singular": "Gram per hour",
         "plural": "Grams per hour",
         "display": "g/h"
      },
      "to_anchor": 1 / 3600,
      "aliases": [
         "g/h"
      ]
   },
   "kg/s": {
      "name": {
         "singular": "Kilogram per second",
         "plural": "Kilograms per second",
         "display": "kg/s"
      },
      "to_anchor": 1000,
      "aliases": [
         "kg/s"
      ]
   },
   "kg/min": {
      "name": {
         "singular": "Kilogram per minute",
         "plural": "Kilograms per minute",
         "display": "kg/min"
      },
      "to_anchor": 1000 / 60,
      "aliases": [
         "kg/min"
      ]
   },
   "kg/h": {
      "name": {
         "singular": "Kilogram per hour",
         "plural": "Kilograms per hour",
         "display": "kg/h"
      },
      "to_anchor": 1000 / 3600,
      "aliases": [
         "kg/h"
      ]
   },
   "ton/s": {
      "name": {
         "singular": "Ton per second",
         "plural": "Tons per second",
         "display": "t/s"
      },
      "to_anchor": 1000 * 1000,
      "aliases": [
         "ton/s"
      ]
   },
   "ton/min": {
      "name": {
         "singular": "Ton per minute",
         "plural": "Tons per minute",
         "display": "t/min"
      },
      "to_anchor": (1000 * 1000) / 60,
      "aliases": [
         "ton/min"
      ]
   },
   "ton/h": {
      "name": {
         "singular": "Ton per hour",
         "plural": "Tons per hour",
         "display": "t/h"
      },
      "to_anchor": (1000 * 1000) / 3600,
      "aliases": [
         "ton/h"
      ]
   }
}

imperial = {
   "oz/s": {
      "name": {
         "singular": "Ounce per second",
         "plural": "Ounces per second",
         "display": "oz/s"
      },
      "to_anchor": 1 / 16,
      "aliases": [
         "oz/s"
      ]
   },
   "oz/min": {
      "name": {
         "singular": "Ounce per minute",
         "plural": "Ounces per minute",
         "display": "oz/min"
      },
      "to_anchor": 1 / (16 * 60),
      "aliases": [
         "oz/min"
      ]
   },
   "oz/h": {
      "name": {
         "singular": "Ounce per hour",
         "plural": "Ounces per hour",
         "display": "oz/h"
      },
      "to_anchor": 1 / (16 * 3600),
      "aliases": [
         "oz/h"
      ]
   },
   "lb/s": {
      "name": {
         "singular": "Pound per second",
         "plural": "Pounds per second",
         "display": "lb/s"
      },
      "to_anchor": 1,
      "aliases": [
         "lb/s"
      ]
   },
   "lb/min": {
      "name": {
         "singular": "Pound per minute",
         "plural": "Pounds per minute",
         "display": "lb/min"
      },
      "to_anchor": 1 / 60,
      "aliases": [
         "lb/min"
      ]
   },
   "lb/h": {
      "name": {
         "singular": "Pound per hour",
         "plural": "Pounds per hour",
         "display": "lb/h"
      },
      "to_anchor": 1 / 3600,
      "aliases": [
         "lb/h"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "g/s",
         "ratio": 1 / 453.592
      },
      "imperial": {
         "unit": "lb/s",
         "ratio": 453.592
      }
   }
}

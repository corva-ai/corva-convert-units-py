metric = {
   "mm2": {
      "name": {
         "singular": "Square Millimeter",
         "plural": "Square Millimeters",
         "display": "mm²"
      },
      "to_anchor": 1 / 1000000,
      "aliases": [
         "mm2"
      ]
   },
   "cm2": {
      "name": {
         "singular": "Centimeter",
         "plural": "Centimeters",
         "display": "cm²"
      },
      "to_anchor": 1 / 10000,
      "aliases": [
         "cm2"
      ]
   },
   "m2": {
      "name": {
         "singular": "Square Meter",
         "plural": "Square Meters",
         "display": "m²"
      },
      "to_anchor": 1,
      "aliases": [
         "m2"
      ]
   },
   "ha": {
      "name": {
         "singular": "Hectare",
         "plural": "Hectares",
         "display": "ha"
      },
      "to_anchor": 10000,
      "aliases": [
         "ha"
      ]
   },
   "km2": {
      "name": {
         "singular": "Square Kilometer",
         "plural": "Square Kilometers",
         "display": "km²"
      },
      "to_anchor": 1000000,
      "aliases": [
         "km2"
      ]
   }
}

imperial = {
   "in2": {
      "name": {
         "singular": "Square Inch",
         "plural": "Square Inches",
         "display": "in²"
      },
      "to_anchor": 1 / 144,
      "aliases": [
         "in2"
      ]
   },
   "yd2": {
      "name": {
         "singular": "Square Yard",
         "plural": "Square Yards",
         "display": "yd²"
      },
      "to_anchor": 9,
      "aliases": [
         "yd2"
      ]
   },
   "ft2": {
      "name": {
         "singular": "Square Foot",
         "plural": "Square Feet",
         "display": "ft²"
      },
      "to_anchor": 1,
      "aliases": [
         "ft2"
      ]
   },
   "ac": {
      "name": {
         "singular": "Acre",
         "plural": "Acres",
         "display": "ac"
      },
      "to_anchor": 43560,
      "aliases": [
         "ac"
      ]
   },
   "mi2": {
      "name": {
         "singular": "Square Mile",
         "plural": "Square Miles",
         "display": "mi²"
      },
      "to_anchor": 27878400,
      "aliases": [
         "mi2"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "m2",
         "ratio": 10.7639
      },
      "imperial": {
         "unit": "ft2",
         "ratio": 1 / 10.7639
      }
   }
}

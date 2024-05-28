metric = imperial = {
   "strokes/min": {
      "name": {
         "singular": "stroke per minute",
         "plural": "stroke per minute",
         "display": "strokes/min"
      },
      "to_anchor": 1,
      "aliases": [
        "strokes/min",
        "spm",
        "1/m"
      ]
   },
   "strokes/sec": {
      "name": {
         "singular": "stroke per second",
         "plural": "stroke per second",
         "display": "strokes/sec"
      },
      "to_anchor": 60,
      "aliases": [
        "strokes/sec",
        "sps",
        "1/s"
      ]
   },
   "strokes/h": {
      "name": {
         "singular": "stroke per hour",
         "plural": "stroke per hour",
         "display": "strokes/h"
      },
      "to_anchor": 1/60,
      "aliases": [
        "strokes/h",
        "sph",
        "1/h"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "strokes/min",
         "ratio": 1
      },
      "imperial": {
         "unit": "strokes/min",
         "ratio": 1
      }
   }
}

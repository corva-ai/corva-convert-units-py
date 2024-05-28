from math import pi

angle = {
   "rad": {
      "name": {
         "singular": "radian",
         "plural": "radians",
         "display": "rad"
      },
      "to_anchor": 180/pi,
      "aliases": [
         "rad"
      ]
   },
   "deg": {
      "name": {
         "singular": "degree",
         "plural": "degrees",
         "display": "deg"
      },
      "to_anchor": 1,
      "aliases": [
         "deg"
      ]
   },
   "grad": {
      "name": {
         "singular": "gradian",
         "plural": "gradians",
         "display": "grad"
      },
      "to_anchor": 9/10,
      "aliases": [
         "grad"
      ]
   },
   "arcmin": {
      "name": {
         "singular": "arcminute",
         "plural": "arcminutes",
         "display": "arcmin"
      },
      "to_anchor": 1/60,
      "aliases": [
         "arcmin"
      ]
   },
   "arcsec": {
      "name": {
         "singular": "arcsecond",
         "plural": "arcseconds",
         "display": "arcsec"
      },
      "to_anchor": 1/3600,
      "aliases": [
         "arcsec"
      ]
   }
}

rule = {
   "metric": angle,
   "imperial": angle,
   "_anchors": {
      "metric": {
         "unit": "deg",
         "ratio": 1
      },
      "imperial": {
         "unit": "deg",
         "ratio": 1
      }
   }
}

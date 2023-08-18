metric = {
   "rpl": {
      "name": {
         "singular": "revolution per litre",
         "plural": "revolution per litre",
         "display": "1/l"
      },
      "to_anchor": 1,
      "aliases": [
         "rpl"
      ]
   }
}

imperial = {
   "rpg": {
      "name": {
         "singular": "revolution per gallon",
         "plural": "revolution per gallon",
         "display": "1/gal"
      },
      "to_anchor": 1,
      "aliases": [
         "rpg"
      ]
   }
}

rule = {
   "metric": metric,
   "imperial": imperial,
   "_anchors": {
      "metric": {
         "unit": "rpl",
         "ratio": 3.78541
      },
      "imperial": {
         "unit": "rpg",
         "ratio": 1 / 3.78541
      }
   }
}

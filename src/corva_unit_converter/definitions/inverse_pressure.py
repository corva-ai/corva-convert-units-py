metric = {
   "i-pa":  {
      "name":  {
         "singular":  "inverse pascal",
         "plural":  "inverse pascals",
         "display":  "1/Pa"
      },
      "to_anchor":  1000,
      "aliases":  [
         "i-pa"
      ]
   },
   "i-kPa":  {
      "name":  {
         "singular":  "inverse kilopascal",
         "plural":  "inverse kilopascals",
         "display":  "1/kPa"
      },
      "to_anchor":  1,
      "aliases":  [
         "i-kPa"
      ]
   },
   "i-bar":  {
      "name":  {
         "singular":  "inverse bar",
         "plural":  "inverse bar",
         "display":  "1/bar"
      },
      "to_anchor":  1/100,
      "aliases":  [
         "i-bar"
      ]
   }
}

imperial = {
   "i-psi":  {
      "name":  {
         "singular":  "inverse pound per square inch",
         "plural":  "inverse pounds per square inch",
         "display":  "1/psi"
      },
      "to_anchor":  1000,
      "aliases":  [
         "i-psi"
      ]
   },
   "i-ksi":  {
      "name":  {
         "singular":  "inverse kilopound per square inch",
         "plural":  "inverse kilopounds per square inch",
         "display":  "1/ksi"
      },
      "to_anchor":  1,
      "aliases":  [
         "i-ksi"
      ]
   }
}

rule = {
   "metric":  metric,
   "imperial":  imperial,
   "_anchors":  {
      "metric":  {
         "unit":  "i-pa",
         "ratio":  6894.757
      },
      "imperial":  {
         "unit":  "i-psi",
         "ratio":  1 / 6894.757
      }
   }
}

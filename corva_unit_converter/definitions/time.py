daysInYear = 365.25

time = {
   "ns": {
      "name": {
         "singular": "Nanosecond",
         "plural": "Nanoseconds",
         "display": "ns"
      },
      "to_anchor": 1 / 1000000000,
      "aliases": [
         "ns"
      ]
   },
   "mu": {
      "name": {
         "singular": "Microsecond",
         "plural": "Microseconds",
         "display": "mu"
      },
      "to_anchor": 1 / 1000000,
      "aliases": [
         "mu"
      ]
   },
   "ms": {
      "name": {
         "singular": "Millisecond",
         "plural": "Milliseconds",
         "display": "ms"
      },
      "to_anchor": 1 / 1000,
      "aliases": [
         "ms"
      ]
   },
   "s": {
      "name": {
         "singular": "Second",
         "plural": "Seconds",
         "display": "s"
      },
      "to_anchor": 1,
      "aliases": [
         "s", "sec"
      ]
   },
   "min": {
      "name": {
         "singular": "Minute",
         "plural": "Minutes",
         "display": "min"
      },
      "to_anchor": 60,
      "aliases": [
         "min"
      ]
   },
   "h": {
      "name": {
         "singular": "Hour",
         "plural": "Hours",
         "display": "hr"
      },
      "to_anchor": 60 * 60,
      "aliases": [
         "h"
      ]
   },
   "d": {
      "name": {
         "singular": "Day",
         "plural": "Days",
         "display": "d"
      },
      "to_anchor": 60 * 60 * 24,
      "aliases": [
         "d", "day"
      ]
   },
   "week": {
      "name": {
         "singular": "Week",
         "plural": "Weeks",
         "display": "w"
      },
      "to_anchor": 60 * 60 * 24 * 7,
      "aliases": [
         "week"
      ]
   },
   "month": {
      "name": {
         "singular": "Month",
         "plural": "Months",
         "display": "m"
      },
      "to_anchor": 60 * 60 * 24 * daysInYear / 12,
      "aliases": [
         "month"
      ]
   },
   "year": {
      "name": {
         "singular": "Year",
         "plural": "Years",
         "display": "yr"
      },
      "to_anchor": 60 * 60 * 24 * daysInYear,
      "aliases": [
         "year"
      ]
   }
}


rule = {
   "metric": time,
   "_anchors": {
      "metric": {
         "unit": "s",
         "ratio": 1
      }
   }
}

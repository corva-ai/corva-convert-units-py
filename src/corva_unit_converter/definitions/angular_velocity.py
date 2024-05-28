# 1/s, rev/s, rpm, rph, rad/s, dega/s, dega/m, dega/h
# NOTE: "a" letter is added to degree to avoid confusion with temperature
#
# to_anchor values might be clearer but the base unit was defined as RPM
from math import pi

metric = {
    "1/s": {
        "name": {
            "singular": "revolution per second",
            "plural": "revolutions per second",
            "display": "1/s"
        },
        "to_anchor": 60,
        "aliases": [
            "1/s",
            "Hz"
        ]
    },
    "rev/s": {
        "name": {
            "singular": "revolution per second",
            "plural": "revolutions per second",
            "display": "1/s"
        },
        "to_anchor": 60,
        "aliases": [
            "rev/s"
        ]
    },
    "rpm": {
        "name": {
            "singular": "revolution per minute",
            "plural": "revolutions per minute",
            "display": "rpm"
        },
        "to_anchor": 1,
        "aliases": [
            "rpm"
        ]
    },
    "rph": {
        "name": {
            "singular": "revolution per hour",
            "plural": "revolutions per hour",
            "display": "rph"
        },
        "to_anchor": 1 / 60,
        "aliases": [
            "rph"
        ]
    },
    "radsec": {
        "name": {
            "singular": "radian per second",
            "plural": "radians per second",
            "display": "rad/sec"
        },
        "to_anchor": 60 / (2 * pi),
        "aliases": [
            "radsec", "rad/s", "rad/sec"
        ]
    },
    "dega/s": {
        "name": {
            "singular": "degree per second",
            "plural": "degrees per second",
            "display": "dega/s"
        },
        "to_anchor": 1 / 6,
        "aliases": [
            "dega/s"
        ]
    },
    "dega/m": {
        "name": {
            "singular": "degree per minute",
            "plural": "degrees per minute",
            "display": "dega/m"
        },
        "to_anchor": 1 / 360,
        "aliases": [
            "dega/m"
        ]
    },
    "dega/h": {
        "name": {
            "singular": "degree per hour",
            "plural": "degrees per hour",
            "display": "dega/h"
        },
        "to_anchor": (1 / 360) / 60,
        "aliases": [
            "dega/h"
        ]
    }
}

rule = {
    "metric": metric,
    "_anchors": {
        "metric": {
            "unit": "rpm",
            "ratio": 1
        },
        "imperial": {
            "unit": "rpm",
            "ratio": 1
        }
    }
}

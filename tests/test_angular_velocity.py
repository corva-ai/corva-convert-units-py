import math

from .utils import convert_units

# test cases
cases = [
    {"from": "rev/s", "amount": 1, "to": "dega/s", "expected": 360},
    {"from": "1/s", "amount": 1, "to": "dega/s", "expected": 360},
    {"from": "rpm", "amount": 1, "to": "dega/s", "expected": 360/60},
    {"from": "rpm", "amount": 1, "to": "dega/m", "expected": 360},
    {"from": "rph", "amount": 1, "to": "dega/m", "expected": 6},
    {"from": "rph", "amount": 1, "to": "dega/s", "expected": 0.1},
    {"from": "rph", "amount": 1, "to": "dega/h", "expected": 360},
    {"from": "dega/s", "amount": 1, "to": "dega/s", "expected": 1},
    {"from": "dega/s", "amount": 1, "to": "dega/m", "expected": 60},
    {"from": "dega/m", "amount": 1, "to": "dega/s", "expected": 1/60},
    {"from": "1/s", "amount": 1, "to": "radsec", "expected": 2*math.pi},
    {"from": "radsec", "amount": 1, "to": "dega/s", "expected": 180/math.pi},
    {"from": "dega/h", "amount": 1, "to": "dega/s", "expected": 1/3600}
]


def test():
    convert_units(cases)

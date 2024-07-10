from .utils import convert_units

# test cases
cases = [
    {"from": "gal/min", "amount": 1, "to": "m3/min", "expected": 0.00378541},
    {"from": "m3/min", "amount": 1, "to": "gal/min", "expected": 264.172},
    {"from": "gal/min", "amount": 1, "to": "ml/30min", "expected": 113562.354},
    {"from": "ml/30min", "amount": 1, "to": "gal/min", "expected": 0.00000880573508},
]


def test():
    convert_units(cases)

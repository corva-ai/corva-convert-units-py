from .utils import convert_units

# test cases
cases = [
    {"from": "%EMA", "amount": 1, "to": "Units (0-5000u)", "expected": 50},
    {"from": "%EMA", "amount": 100, "to": "Units (0-5000u)", "expected": 5000},
    {"from": "%EMA", "amount": 100, "to": "Units (0-10000u)", "expected": 10000},
    {"from": "Units (0-10000u)", "amount": 100, "to": "Units (0-5000u)", "expected": 50},
    {"from": "%EMA", "amount": 1, "to": "ppm", "expected": 10000},
    {"from": "%", "amount": 1, "to": "%EMA", "expected": 1},
    {"from": "%", "amount": 1, "to": "Units", "expected": 50},
    {"from": "Units", "amount": 50, "to": "%EMA", "expected": 1}
]


def test():
    convert_units(cases)

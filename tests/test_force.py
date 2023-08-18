from .utils import convert_units

# test cases
cases = [
    {"from": "klbf", "amount": 1, "to": "kdaN", "expected": 0.44482216152547716},
    {"from": "kdaN", "amount": 1, "to": "klbf", "expected": 2.248089438709618},
    {"from": "klbf", "amount": 1, "to": "lbf", "expected": 1000},
    {"from": "kdaN", "amount": 1, "to": "daN", "expected": 1000},
]


def test():
    convert_units(cases)

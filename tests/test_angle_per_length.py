from .utils import convert_units

# test cases
cases = [
    {"from": "dpm", "amount": 1, "to": "dpf", "expected": 0.304799990},
    {"from": "dpf", "amount": 1, "to": "dpm", "expected": 3.28084},
    {"from": "dp100f", "amount": 1, "to": "dp30m", "expected": 0.984252},
    {"from": "dp30m", "amount": 1, "to": "dp100f", "expected": 1.015999967488001},
]


def test():
    convert_units(cases)

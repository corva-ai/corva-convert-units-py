from .utils import convert_units

# test cases
cases = [
    {"from": "%", "amount": 1, "to": "Fraction", "expected": 0.01,
     "measure": 'proportion'},
    {"from": "Fraction", "amount": 1, "to": '%', "expected": 100,
     "measure": 'proportion'},
]


def test():
    convert_units(cases)

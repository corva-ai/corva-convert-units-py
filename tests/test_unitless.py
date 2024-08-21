from .utils import convert_units

# test cases
cases = [
    {"from": "unitless", "amount": 1, "to": "unitless", "expected": 1,
     "measure": 'unitless'}
]


def test():
    convert_units(cases)

from .utils import convert_units

# test cases
cases = [
   {"from": "ft", "amount": 1, "to": "m", "expected": 0.3048},
   {"from": "ft", "amount": 1, "to": "yd", "expected": 0.333333},
   {"from": "yd", "amount": 1, "to": "ft", "expected": 3},
   {"from": "m", "amount": 1, "to": "ft", "expected": 3.28084},
   {"from": "km", "amount": 1, "to": "m", "expected": 1000},
   {"from": "km", "amount": 1, "to": "mi", "expected": 0.621371},
   {"from": "mi", "amount": 1, "to": "km", "expected": 1.609343502101154},
   {"from": "in", "amount": 1, "to": "mm", "expected": 25.4},
   {"from": "mm", "amount": 1, "to": "in", "expected": 0.0393701},
]


def test():
    convert_units(cases)

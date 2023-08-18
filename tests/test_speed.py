from .utils import convert_units

# test cases
cases = [
    {"from": "ft/h", "amount": 1, "to": "m/h", "expected": 0.3048},
    {"from": "m/h", "amount": 1, "to": "ft/h", "expected": 3.28084},
    {"from": "mph", "amount": 1, "to": "kph", "expected": 1.609344},
    {"from": "kph", "amount": 1, "to": "mph", "expected": 0.621371},
    {"from": "ft/min", "amount": 1, "to": "m/min", "expected": 0.30479902464},
    {"from": "m/min", "amount": 1, "to": "ft/min", "expected": 3.28085039373},
]


def test():
    convert_units(cases)

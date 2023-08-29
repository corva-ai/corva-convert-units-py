from .utils import convert_units

# test cases
cases = [
    {"from": "ft-klbf", "amount": 1, "to": "Nm", "expected": 1355.8179483},
    {"from": "Nm", "amount": 1, "to": "ft-klbf", "expected": 0.0007375621493},
    {"from": "ft-klbf", "amount": 1, "to": "kNm", "expected": 1.3558179483},
    {"from": "kNm", "amount": 1, "to": "ft-klbf", "expected": 0.7375621493},
    {"from": "Nm", "amount": 1, "to": "J", "expected": 1.},
]


def test():
    convert_units(cases)

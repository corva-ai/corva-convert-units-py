from .utils import convert_units

cases = [
    {"from": "mpas", "amount": 1, "to": "pas", "expected": 0.001},
    {"from": "pas", "amount": 1, "to": "mpas", "expected": 1000},
]


def test():
    convert_units(cases)

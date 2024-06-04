from .utils import convert_units

# test cases
cases = [
    {"from": "Mscf", "amount": 5.5, "to": "m3", "expected": 155.807365439093,
     "measure": 'gas_volume'},
    {"from": "Mscf", "amount": 5.5, "to": "ft3", "expected": 0.0055,
     "measure": 'gas_volume'},
    {"from": "bbl", "amount": 1, "to": "m3", "expected": 0.1586402266,
     "measure": 'gas_volume'},
    {"from": "m3", "amount": 1, "to": "bbl", "expected": 6.30357142857,
     "measure": 'gas_volume'}
]


def test():
    convert_units(cases)

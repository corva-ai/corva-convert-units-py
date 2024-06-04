from .utils import convert_units

# test cases
cases = [
    {"from": "%EMA", "amount": 1, "to": "Units (0-5000u)", "expected": 50,
     "measure": 'gas_concentration'},
    {"from": "%EMA", "amount": 100, "to": "Units (0-5000u)", "expected": 5000,
     "measure": 'gas_concentration'},
    {"from": "%EMA", "amount": 100, "to": "Units (0-10000u)",
     "expected": 10000, "measure": 'gas_concentration'},
    {"from": "Units (0-10000u)", "amount": 100, "to": "Units (0-5000u)",
     "expected": 50, "measure": 'gas_concentration'},
    {"from": "%EMA", "amount": 1, "to": "ppm", "expected": 10000,
     "measure": 'gas_concentration'},
    {"from": "%", "amount": 1, "to": "%EMA", "expected": 1,
     "measure": 'gas_concentration'},
    {"from": "%", "amount": 1, "to": "Units", "expected": 50,
     "measure": 'gas_concentration'},
    {"from": "Units", "amount": 50, "to": "%EMA", "expected": 1,
     "measure": 'gas_concentration'}
]


def test():
    convert_units(cases)

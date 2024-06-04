from .utils import convert_units

# test cases
cases = [
    {"from": "lb/gal", "amount": 1, "to": "kg/m3", "expected": 119.82639999,
     "measure": 'density'},
    {"from": "kg/m3", "amount": 1, "to": "lb/gal", "expected": 0.0083454,
     "measure": 'density'},
    {"from": "Sg", "amount": 1, "to": "g/cm3", "expected": 1,
     "measure": 'density'},
    {"from": "Sg", "amount": 1, "to": "g/l", "expected": 1000,
     "measure": 'density'},
    {"from": "Sg", "amount": 1, "to": "g/m3", "expected": 1000000,
     "measure": 'density'},
    {"from": "Sg", "amount": 1, "to": "lb/ft3", "expected": 62.42797480788442,
     "measure": 'density'},
    {"from": "Sg", "amount": 1, "to": "lb/in3", "expected": 0.03612729292702749,
     "measure": 'density'},
    {"from": "ppg", "amount": 1, "to": "g/cm3", "expected": 0.119826427,
     "measure": 'density'},
    {"from": "ppg", "amount": 1, "to": "g/l", "expected": 119.826427,
     "measure": 'density'},
    {"from": "ppg", "amount": 1, "to": "g/m3", "expected": 119826.4,
     "measure": 'density'},
    {"from": "ppg", "amount": 1, "to": "lb/ft3", "expected": 7.48051963537325637,
     "measure": 'density'},
    {"from": "ppg", "amount": 1, "to": "lb/in3", "expected": 0.00432900442862808,
     "measure": 'density'},
    # {"from": "lb/Mgal", "amount": 1, "to": "kg/m3", "expected": 119826.4},
    # {"from": "kg/m3", "amount": 1, "to": "lb/Mgal", "expected": 8.3454e-06}
]


def test():
    convert_units(cases)

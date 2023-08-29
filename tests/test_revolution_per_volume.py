from .utils import convert_units

# test cases
cases = [
    {"from": "rpg", "amount": 1, "to": "rpl", "expected": 0.26417217685798894},
    {"from": "rpl", "amount": 1, "to": "rpg", "expected": 3.78541},
]


def test():
    convert_units(cases)

from .utils import convert_units

# Test cases
cases = [
    {"from": "strokes/min", "amount": 1, "to": "strokes/sec",
     "expected": 0.016666666666666666},
    {"from": "strokes/min", "amount": 1, "to": "strokes/h", "expected": 60},

    {"from": "strokes/sec", "amount": 1, "to": "strokes/min", "expected": 60},
    {"from": "strokes/sec", "amount": 1, "to": "strokes/h", "expected": 3600},

    {"from": "strokes/h", "amount": 1, "to": "strokes/sec",
     "expected": 0.0002777777777777778},
    {"from": "strokes/h", "amount": 1, "to": "strokes/min",
     "expected": 0.016666666666666666},
]


def test():
    convert_units(cases)

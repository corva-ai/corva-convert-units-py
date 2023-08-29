import math

from corva_unit_converter.converter import Converter


def convert_units(cases: list):
    converter = Converter()
    for case in cases:
        result = converter.convert(case["from"], case["to"], case["amount"])
        print(result)
        assert math.isclose(result, case["expected"], rel_tol=1e-06)

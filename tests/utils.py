import math

from src.corva_unit_converter.converter import Converter


def convert_units(cases: list):
    converter = Converter()
    for case in cases:
        measure = case["measure"] if "measure" in case else None

        result = converter.convert(case["from"], case["to"], case["amount"],
                                   measure)
        assert math.isclose(result, case["expected"], rel_tol=1e-06)

# Units Converter

A handy utility for converting between quantities in different units.

This is a python version of the existing javascript app.
Credit goes to the creator and contributors of the original version https://github.com/corva-ai/corva-convert-units

Usage:

Imperial to metric:

    from corva_unit_converter.converter import Converter
    converter = Converter()
    length_meters = converter.convert(unit_from="ft", unit_to="m", value=1)

Metric to imperial:

    from corva_unit_converter.converter import Converter
    converter = Converter()
    torque_ft_lbf = converter.convert(unit_from="Nm", unit_to="ft-lbf", value=1)

Metric to metric:

    from corva_unit_converter.converter import Converter
    converter = Converter()
    mass_grams = converter.convert(unit_from="kg", unit_to="g", value=1)

# Units Converter

Library for converting between quantities in different units(including units specific to O&G).

This is a python version of the existing javascript app.
Credit goes to the creator and contributors of the original version https://github.com/corva-ai/corva-convert-units,
which is a fork of https://github.com/convert-units/convert-units.

# Installation

```shell
pip install corva-unit-converter
```

# Usage:

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


# Testing

1. Create virtualenv via your favourite tool, for example 
```shell
python3 -m venv venv
source venv/bin/activate
```
2. Install all requirements:
```shell
pip install -r requirements.txt && pip install -r requirements-test.txt
```
3. Run tests with coverage:
```shell
make coverage
```
or tests without coverage:
```shell
make test
```
Linters are available through
```shell
make lint
```

# License
This project is licensed under the terms of the MIT license.

Copyright (c) 2013-2017 Ben Ng and Contributors, http://benng.me

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
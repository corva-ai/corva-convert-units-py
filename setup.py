import pathlib
from importlib import machinery

import setuptools

ROOT = pathlib.Path(__file__).parent


VERSION = str(
    machinery.SourceFileLoader('version', 'src/version.py').load_module().VERSION
)

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Topic :: Software Development :: Libraries',
]

setuptools.setup(
    name="corva-unit-converter",
    author="Yuliya Klimushina",
    author_email="yuliya.klimushina@corva.ai",
    url="https://github.com/corva-ai/corva-convert-units-py",
    version=VERSION,
    classifiers=CLASSIFIERS,
    description="Unit converter for O&G(and other) units",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="corva, unit converter",
    py_modules=[file.stem for file in pathlib.Path("src").glob("*.py")],
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.8, <4.0",
    license="MIT",
)

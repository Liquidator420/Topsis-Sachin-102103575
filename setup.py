import pathlib
from setuptools import setup, find_packages

HERE=pathlib.path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='TOPSIS-Sachin-102103575',
    version='0.1',
    description='It does a topsis analysis of a given csv file'
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/uditvashisht/saral-square",
    author="Udit Vashisht",
    author_email="admin@saralgyaan.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
)

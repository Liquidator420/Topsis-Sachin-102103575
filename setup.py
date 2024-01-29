import pathlib
from setuptools import setup, find_packages

HERE=pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='Topsis_Sachin_102103575',
    version='0.3',
    description='It does a topsis analysis of a given csv file',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Liquidator420/Topsis-Sachin-102103575",
    author="Sachin Sushil Singh",
    author_email="sachinsushilsingh@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=["analysis"],
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
    ],
    entry_points={
        "console_scripts": [
            "analysis=analysis.__main__:main",
        ]
    },
)
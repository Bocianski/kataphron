from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Kataphron Python package'
LONG_DESCRIPTION = 'My first Python package about Cult Mechanicum'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="kataphron",
    version=VERSION,
    author="Bocianski",
    author_email="szyper999@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    #install_requires=open("requirements.txt").readlines(),

    keywords=['python', 'kataphron', 'warhammer40k'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
from setuptools import setup, find_packages

setup(
    name='dcvalidator',
    packages=find_packages(exclude=['unit_tests*']),
    install_requires=[
        "python-Levenshtein",
        "ruamel.yaml",
    ],
    entry_points={
        'console_scripts': ['dcvalidator = dcvalidator.validator-cli:main'],
    },
    classifiers=[
        'Private :: Do Not Upload :: This line make sure that you do not accidentally upload stuff to the real PyPI',
    ]

)

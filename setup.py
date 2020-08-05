from setuptools import setup, find_packages

setup(
    name='dcvalidator',
    packages=['dcvalidator', ],
    install_requires=[
        "python-Levenshtein",
        "ruamel.yaml",
        "pyyaml"
    ],
    entry_points={
        'console_scripts': ['dcvalidator = dcvalidator.cli:main'],
    },
    classifiers=[
        'Private :: Do Not Upload :: This line make sure that you do not accidentally upload stuff to the real PyPI',
    ]

)

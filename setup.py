from setuptools import setup

setup(
    name='ksd',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'ksd=main:main'
        ]
    }
)

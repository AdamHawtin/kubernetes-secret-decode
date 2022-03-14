from setuptools import setup

setup(
    name='ksd',
    version='0.2.0',
    entry_points={
        'console_scripts': [
            'ksd=main:main'
        ]
    }
)

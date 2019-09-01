from setuptools import setup

setup(
    name='ksd',
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'ksd=main:main'
        ]
    }
)

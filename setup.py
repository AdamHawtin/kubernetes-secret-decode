from setuptools import setup

setup(
    name='ksd',
    version='0.2.1',
    entry_points={
        'console_scripts': [
            'ksd=main:main'
        ]
    },
    py_modules=[],
    python_requires=">=3.10",
)

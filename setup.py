from setuptools import setup, find_packages

setup(
    name='fittrack',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'fittrack=fittrack.cli:main',
        ],
    },
)

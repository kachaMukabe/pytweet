from setuptools import setup, find_packages

setup(
    name='pytweet',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'rich'
    ],
    entry_points='''
        [console_scripts]
        pytweet=src.cli:cli
    ''',
)
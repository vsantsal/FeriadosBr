from setuptools import find_packages, setup

setup(
    name='feriados',
    version='0.1.0',
    packages=find_packages(include=['feriados']),
    author='Vinícius Salustiano',
    package_dir={'': 'src'},
)

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='comp0034-cw2-i-KevinHe0805',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements
)

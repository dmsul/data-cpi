from setuptools import setup, find_packages

from data_cpi.util.env import PROJECT_NAME


dependencies: list = [
    # 'econtools',
]

setup(
    name=PROJECT_NAME,
    version='0.0.1',
    description='Access to CPI data.',
    author='Daniel M. Sullivan',
    packages=find_packages(),
    tests_require=[
        'pytest',
    ],
    package_data={PROJECT_NAME.replace('-', '_'): ["py.typed"]},
    install_requires=dependencies,
    zip_safe=False,
    license='BSD'
)

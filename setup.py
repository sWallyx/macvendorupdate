from setuptools import setup

setup(
    name='macvendorupdate',
    packages=['macvendorupdate'],
    version='0.2',
    description='Scripts to update the mac address brand list',
    author='sWallyx',
    keywords=['mac address', 'wifi', 'brands', 'people'],
    classifiers=[],
    install_requires=["click", "mysql-connector-python"],
    setup_requires=[],
    tests_require=[],
)

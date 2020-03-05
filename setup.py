from setuptools import setup

setup(
    name='macvendorupdate',
    version='0.2.5',
    description='Scripts to update the mac address brand list to a Python file or a MySQL DataBase',
    author='sWallyx',
    keywords=['mac address', 'wifi', 'brands', 'people', 'oui', 'devices', 'python', 'mysql'],
    classifiers=[],
    install_requires=["click", "mysql-connector-python"],
    setup_requires=[],
    tests_require=[],
)

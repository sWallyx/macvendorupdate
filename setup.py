from setuptools import setup, find_packages

setup(
    name='macvendorupdate',
    version='0.2.6',
    description='Scripts to update the mac address brand list to a Python file or a MySQL DataBase',
    author='sWallyx',
    keywords=['mac address', 'wifi', 'brands', 'people', 'oui', 'devices', 'python', 'mysql', 'download'],
    classifiers=[],
    install_requires=["click", "mysql-connector-python", "pytest"],
    setup_requires=[],
    tests_require=[],
    packages=find_packages(),
)

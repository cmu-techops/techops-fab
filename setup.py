from setuptools import setup
setup(
    name='techops.fab',
    version='0.3',
    packages=['techops.fab'],
    package_data = {'techops.fab': []},
    namespace_packages=['techops'],
    install_requires=["Fabric>=1.6"],
    zip_safe=False,
)

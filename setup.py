import sys
from setuptools import setup, find_packages

#next time:
#python setup.py register
#python setup.py sdist upload

version = open('thunderdome_logging/VERSION', 'r').readline().strip()

long_desc = """
Extension for thunderdome which allows error logging in the graph.
"""

setup(
    name='thunderdome-logging',
    version=version,
    description='Thunderdome graph error logging',
    dependency_links=['https://github.com/StartTheShift/thunderdome-logging/archive/{0}.tar.gz#egg=thunderdome-logging-{0}'.format(version)],
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='cassandra,titan,ogm,thunderdome,logging',
    install_requires=['thunderdome==0.4.3'],
    author='StartTheShift',
    author_email='dev@shift.com',
    url='https://github.com/StartTheShift/thunderdome-logging',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
)

from setuptools import setup, find_packages
import os

# get long description
if os.path.isfile('README.rst'):
    with open('README.rst', 'r') as file:
        long_description = file.read()
else:
    long_description = ''

# get version
with open('nose2unitth/VERSION', 'r') as file:
    version = file.read().strip()

# parse dependencies and their links from requirements.txt files
install_requires = [line.rstrip() for line in open('requirements.txt')]
tests_require = [line.rstrip() for line in open('tests/requirements.txt')]

# install package
setup(
    name="nose2unitth",
    version=version,
    description="Convert nose-style test reports to UnitTH-style test reports",
    long_description=long_description,
    url="https://github.com/KarrLab/nose2unitth",
    download_url='https://github.com/KarrLab/nose2unitth',
    author="Jonathan Karr",
    author_email="jonrkarr@gmail.com",
    license="MIT",
    keywords='nose unitth xunit junit',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={
        'nose2unitth': [
            'VERSION',
        ],
    },
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
            'nose2unitth = nose2unitth.__main__:main',
        ],
    },
)

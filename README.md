# nose2unitth
Convert [nose](http://nose.readthedocs.io)-style XML test reports to [UnitTH](http://junitth.sourceforge.net/)-compatible XML reports

## Example
* [nose-style XML report](examples/nose.xml)
* [UnitTH-style XML report](examples/unitth/1)
* [UnitTH HTML test history report](https://cdn.rawgit.com/KarrLab/nose2unitth/master/examples/html/index.html)

## Installation
```
pip install nose2unitth
```

[![PyPI package](https://badge.fury.io/py/nose2unitth.svg)](https://pypi.python.org/pypi/nose2unitth)

## Usage
```
# convert nose-style reports to UnitTH-style reports
nosetests <package-to-test> --with-xunit --xunit-file=examples/nose.xml

mkdir -p examples/unitth
nose2unitth examples/nose.xml examples/unitth/1
nose2unitth examples/nose.xml examples/unitth/2

junit2html examples/nose.xml examples/unitth/1/index.html
junit2html examples/nose.xml examples/unitth/2/index.html

# generate HTML test report
java \
    -Dunitth.generate.exectimegraphs=true \
    -Dunitth.xml.report.filter= \
    -Dunitth.html.report.path=. \
    -Dunitth.report.dir=examples/html \
    -jar unitth.jar examples/unitth/*
```

## Documentation
Please see the documentation at [Read the Docs](http://nose2unitth.readthedocs.io).

[![Documentation](https://readthedocs.org/projects/nose2unitth/badge/?version=latest)](http://nose2unitth.readthedocs.io)

## Tests
### Running the tests
`nose` can be used to run the tests:
```
nosetests tests \
  --with-xunit --xunit-file=test-report.xml \
  --with-coverage --cover-package=nose2unitth
```

Please note that additional packages are required for testing (see [tests/requirements.txt] (tests/requirements.txt)).

### Test report
[![Test status](https://circleci.com/gh/KarrLab/nose2unitth.svg?style=shield)](https://circleci.com/gh/KarrLab/nose2unitth)

### Coverage report
[![Coverage Status](https://coveralls.io/repos/github/KarrLab/nose2unitth/badge.svg)](https://coveralls.io/github/KarrLab/nose2unitth)

## License
The example model is released under the [MIT license](LICENSE.txt).

## Development team
`nose2unitth` was developed by [Jonathan Karr](http://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York, USA.

## Questions and comments
Please contact the [Jonathan Karr](http://www.karrlab.org) with any questions or comments.

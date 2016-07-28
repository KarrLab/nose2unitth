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

## License
The example model is released under the [MIT license](LICENSE.txt).

## Development team
`nose2unitth` was developed by [Jonathan Karr](http://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York, USA.

## Questions and comments
Please contact the [Jonathan Karr](http://www.karrlab.org) with any questions or comments.

Example inputs and outputs
==========================

* `nose-style XML report <../../../examples/nose.xml>`_
* `UnitTH-style XML report <../../../examples/unitth/1/>`_
* `UnitTH HTML test history report <https://cdn.rawgit.com/KarrLab/nose2unitth/master/examples/html/index.html>`_

Command line usage
==========================

.. code-block:: text

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


Testing the package
==========================
`nose` can be used to run the tests:

.. code-block:: text

    nosetests tests \
      --with-xunit --xunit-file=test-report.xml \
      --with-coverage --cover-package=nose2unitth
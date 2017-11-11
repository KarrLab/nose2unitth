""" Tests nose2unitth.

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-08-01
:Copyright: 2016, Karr Lab
:License: MIT
"""

from __future__ import unicode_literals
from nose2unitth.__main__ import App as nose2unitth_cli
from nose2unitth.core import Converter
from xml.dom import minidom
import os
import mock
import nose2unitth
import shutil
import tempfile
import unittest


NOSE_FIXTURE_FILE_NAME = "tests/fixtures/nose.xml"
NOSE_FIXTURE_OBJ = expected_report = {
    "package1.Class1": [
        {"name": "test_pass1", "time": 0.001},
    ],
    "package2.Class2": [
        {"name": "test_pass2", "time": 0.001},
    ],
    "package3.Class3": [
        {"name": "test_error1", "time": 0.001, "error": {
            "type": "exceptions.Exception",
            "message": "test error",
            "text": "Traceback ...\n",
        }
        },
        {"name": "test_failure1", "time": 0.002, "failure": {
            "type": "exceptions.AssertionError",
            "message": "True is not false",
            "text": "Traceback ...\n",
        }
        },
        {"name": "test_skip1", "time": 0.003, "skipped": {
            "type": "unittest.case.SkipTest",
            "message": "test skip",
            "text": "SkipTest: ...\n",
        }
        },
    ],
    "package4.Class4": [
        {"name": "test_pass3", "time": 0.001},
        {"name": "test_pass4", "time": 0.000},
    ],
    "package5.Class5": [
        {"name": "test_failure2", "time": 0.001, "failure": {
            "type": "",
            "message": "True is not false",
            "text": "Traceback ...\n",
        }
        },
    ],
    "package6.Class6": [
        {"name": "test_skip6", "time": 0.001, "skipped": {
            "type": "",
            "message": "test skip",
            "text": "test skip",
        }
        },
        {"name": "test_error6", "time": 0.001, "error": {
            "type": "",
            "message": "test error",
            "text": "test error",
        }
        },
    ],
}

NOSE_FIXTURE_XML = {
    'package1.Class1': """"""
    + """<?xml version="1.0" encoding="utf-8"?>"""
    + """<testsuite errors="0" failures="0" name="package1.Class1" skipped="0" tests="1" time="0.001">"""
    + """<testcase classname="package1.Class1" name="test_pass1" time="0.001"/>"""
    + """</testsuite>""",
    'package2.Class2': """"""
    + """<?xml version="1.0" encoding="utf-8"?>"""
    + """<testsuite errors="0" failures="0" name="package2.Class2" skipped="0" tests="1" time="0.001">"""
    + """<testcase classname="package2.Class2" name="test_pass2" time="0.001"/>"""
    + """</testsuite>""",
    'package3.Class3': """"""
    + """<?xml version="1.0" encoding="utf-8"?>"""
    + """<testsuite errors="1" failures="1" name="package3.Class3" skipped="1" tests="3" time="0.006">"""
    + """<testcase classname="package3.Class3" name="test_error1" time="0.001"><error message="test error" type="exceptions.Exception"><![CDATA[Traceback ...\n]]></error></testcase>"""
    + """<testcase classname="package3.Class3" name="test_failure1" time="0.002"><failure message="True is not false" type="exceptions.AssertionError"><![CDATA[Traceback ...\n]]></failure></testcase>"""
    + """<testcase classname="package3.Class3" name="test_skip1" time="0.003"><skipped message="test skip" type="unittest.case.SkipTest"><![CDATA[SkipTest: ...\n]]></skipped></testcase>"""
    + """</testsuite>""",
    'package4.Class4': """"""
    + """<?xml version="1.0" encoding="utf-8"?>"""
    + """<testsuite errors="0" failures="0" name="package4.Class4" skipped="0" tests="2" time="0.001">"""
    + """<testcase classname="package4.Class4" name="test_pass3" time="0.001"/>"""
    + """<testcase classname="package4.Class4" name="test_pass4" time="0.000"/>"""
    + """</testsuite>""",
    'package5.Class5': """"""
    + """<?xml version="1.0" encoding="utf-8"?>"""
    + """<testsuite errors="0" failures="1" name="package5.Class5" skipped="0" tests="1" time="0.001">"""
    + """<testcase classname="package5.Class5" name="test_failure2" time="0.001"><failure message="True is not false" type=""><![CDATA[Traceback ...\n]]></failure></testcase>"""
    + """</testsuite>""",
    'package6.Class6': """"""
    + """<?xml version="1.0" encoding="utf-8"?>"""
    + """<testsuite errors="1" failures="0" name="package6.Class6" skipped="1" tests="2" time="0.002">"""
    + """<testcase classname="package6.Class6" name="test_skip6" time="0.001"><skipped message="test skip" type=""><![CDATA[test skip]]></skipped></testcase>"""
    + """<testcase classname="package6.Class6" name="test_error6" time="0.001"><error message="test error" type=""><![CDATA[test error]]></error></testcase>"""
    + """</testsuite>""",
}


class TestNose2UnitTH(unittest.TestCase):

    def test_read_nose(self):
        report = Converter.read_nose(NOSE_FIXTURE_FILE_NAME)

        for key, val in NOSE_FIXTURE_OBJ.items():
            self.assertEqual(NOSE_FIXTURE_OBJ[key], report[key])

        self.assertEqual(NOSE_FIXTURE_OBJ, report)

    def test_write_unitth(self):
        out_dir = tempfile.mkdtemp()
        shutil.rmtree(out_dir)
        
        Converter.write_unitth(NOSE_FIXTURE_OBJ, out_dir)

        # 1 XML file per suite
        self.assertEqual(set(NOSE_FIXTURE_OBJ.keys()), set([x.replace('.xml', '') for x in os.listdir(out_dir)]))

        # XML files have tests
        for suite_name in NOSE_FIXTURE_OBJ:
            with open(os.path.join(out_dir, '{}.xml'.format(suite_name)), 'r') as report:
                self.assertEqual(NOSE_FIXTURE_XML[suite_name], report.read())

        # cleanup
        shutil.rmtree(out_dir)

    def test_cli(self):
        out_dir = tempfile.mkdtemp()
        with nose2unitth_cli(argv=[NOSE_FIXTURE_FILE_NAME, out_dir]) as app:
            app.run()

        # 1 XML file per suite
        self.assertEqual(set(NOSE_FIXTURE_OBJ.keys()), set([x.replace('.xml', '') for x in os.listdir(out_dir)]))

        # XML files have tests
        for suite_name in NOSE_FIXTURE_OBJ:
            with open(os.path.join(out_dir, '{}.xml'.format(suite_name)), 'r') as report:
                self.assertEqual(NOSE_FIXTURE_XML[suite_name], report.read())

        # cleanup
        shutil.rmtree(out_dir)

    def test_raw_cli(self):
        with mock.patch('sys.argv', ['nose2unitth', '--help']):
            with self.assertRaises(SystemExit) as context:
                nose2unitth.__main__.main()
                self.assertRegexpMatches(context.Exception, 'usage: nose2unitth')

# -*- coding: utf8 -*-
import os
import sys
from django.test.simple import DjangoTestSuiteRunner
from django.test.utils import setup_test_environment


def runtests(*test_args, **kwargs):
    setup_test_environment()
    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)
    test_runner = DjangoTestSuiteRunner(
        verbosity=kwargs.get('verbosity', 1),
        interactive=kwargs.get('interactive', False),
        failfast=kwargs.get('failfast')
    )
    failures = test_runner.run_tests(test_args)
    sys.exit(failures)
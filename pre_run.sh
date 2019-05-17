#!/bin/bash

#pytest --cov=.
pytest --cov=. --cov-report html:coverage
#pytest --junitxml=pytest/test_output.xml --cov=. --cov-report html:coverage
#pytest --cov=. --cov-report xml:coverage.xml
#pytest
#pylint src
#pylint --rcfile=~/.pylintrc src > pylint.log
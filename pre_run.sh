#!/bin/bash

#pytest --cov=.
pytest --cov=. --cov-report html:coverage
#pylint --rcfile=.pylintrc  src
#pytest --junitxml=pytest/test_output.xml --cov=. --cov-report html:coverage
#pytest --cov=. --cov-report xml:coverage.xml
#pytest
#pylint src
#pylint --rcfile=~/.pylintrc src > pylint.log
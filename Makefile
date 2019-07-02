run:
	python -m src

test:
	ENV=test python -m unittest

coverage:
	ENV=test coverage run -m unittest

coverage-upload:
	ENV=test coverage run -m unittest
	coverage xml
	python-codacy-coverage -r coverage.xml

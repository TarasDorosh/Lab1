all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	pip install pipenv
	pipenv --python 3.8
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	@echo "Start tests."
	pipenv run python3 app.py > results.txt

run:
	@echo "Run python app."
	pipenv run pytest tests/tests.py >> results.txt

deploy:
	@echo "Adding and committing results.txt"
	git add results.txt
	git commit -m "laboratorna2: Вносимо дані в result.txt"
	git push

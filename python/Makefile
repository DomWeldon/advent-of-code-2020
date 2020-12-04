

.PHONY: setup
setup:
	poetry install


.PHONY: repl
repl:
	poetry run bpython


.PHONY: fix
fix:
	poetry run black day* ./*.py utils -l 79
	poetry run isort .


.PHONY: lint
lint:
	poetry run flake8 challenge


.PHONY: test
test:
	poetry run pytest ./

.PHONY: run
run:
	poetry run python -m challenge

.PHONY: run test help

PRG_RUN=./main.py
PRG_RUN_TEST=./tests.py

run:
	rm -f __pycache__ ; $(PRG_RUN)

help:
	$(PRG_RUN) help

config:
	$(PRG_RUN) config

test:
	$(PRG_RUN_TEST)
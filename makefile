.PHONY: run test help readlog config

PRG_RUN=./source/main.py
PRG_RUN_TEST=./source/tests.py
PRG_LOG=./source/processLog.py
LOG_FILE=log/log.log

run:
	rm -f __pycache__ ; $(PRG_RUN) &

runf:
	rm -f __pycache__ ; $(PRG_RUN)

help:
	$(PRG_RUN) help

config:
	$(PRG_RUN) config

test:
	$(PRG_RUN_TEST)

# take log file and output some cool info to console
readlog:
	@$(PRG_LOG) $(LOG_FILE)

readlog1:
	@$(PRG_LOG) $(LOG_FILE) -d 1
#logtoday: # or just add parameter argument for processLog.py (last day + debug levels)

readlog2:
	@$(PRG_LOG) $(LOG_FILE) -d 2

readlog3:
	@$(PRG_LOG) $(LOG_FILE) -d 3

diff:
	@./source/timeControl.py

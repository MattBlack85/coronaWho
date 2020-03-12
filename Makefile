PIPENV_RUN = pipenv run

.PHONY: bootstrap \
	cheeseshop \
	nuke-venv \
	run \

bootstrap: nuke-venv cheeseshop

cheeseshop:
	@pipenv install --dev

nuke-venv:
	@pipenv --rm;\
	EXIT_CODE=$$?;\
	if [ $$EXIT_CODE -eq 1 ]; then\
		echo Skipping virtualenv removal;\
	fi

run:
	@$(PIPENV_RUN) python corona.py

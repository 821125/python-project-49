brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calcmak

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

shell:
	poetry shell

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

pip install poetry

poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

coverage run --source=api -m pytest tests/

coveralls

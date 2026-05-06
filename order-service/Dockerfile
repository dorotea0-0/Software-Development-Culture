FROM python:3.12-slim

WORKDIR /app

# Копируем только pyproject.toml (без poetry.lock)
COPY pyproject.toml ./

# Устанавливаем Poetry и генерируем lock-файл заново
RUN pip install poetry && poetry lock && poetry install --only main --no-root

COPY src/app ./app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
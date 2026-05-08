FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install uv && uv pip install --system --no-cache -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]

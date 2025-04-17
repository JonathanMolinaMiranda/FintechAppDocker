FROM python:3.10-slim

WORKDIR /app

COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api/api.py .

CMD ["python", "api.py"]
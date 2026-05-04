FROM python:3.9-slim

WORKDIR /app

COPY main.py .
RUN pip install fastapi uvicorn

EXPOSE 8000

CMD ["uvicorn", "main.py", "--host", "0.0.0.0", "--port", "8000"]

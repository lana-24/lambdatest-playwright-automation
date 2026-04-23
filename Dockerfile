FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install chromium
RUN apt-get update && apt-get install -y libgbm1
COPY . .

CMD ["pytest", "tests/", "-v"]
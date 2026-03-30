FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["python", "main.py", "-d", "hailstone", "-v", "single", "-p", "27", "-l", "0"]
# For interactive use: docker run -it hailstone-numbers /bin/bash
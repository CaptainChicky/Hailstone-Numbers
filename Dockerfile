FROM python:3.11.4
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD ["python", "main.py", "-d", "hailstone", "-v", "single", "-p", "27", "-l", "0", "-t"]
# this will timeout the first script so you can run others without the --timeout flag
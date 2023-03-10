# Define the Dockerfile content
dockerfile = """
FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "main.py"]
"""


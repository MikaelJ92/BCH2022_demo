
FROM Python:latest

COPY requirements.txt ./
RUN pip install -r requirements

COPY . .

CMD ["python", "./app.py"]
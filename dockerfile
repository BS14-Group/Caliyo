FROM python:3.10

WORKDIR /
COPY . .

RUN pip install psutil

ENTRYPOINT ["python"]
CMD ["main.py"]
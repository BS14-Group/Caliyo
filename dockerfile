FROM python:3.10

WORKDIR /
COPY . .

RUN pip install psutil requests

ENTRYPOINT ["python"]
CMD ["-u","main.py"]

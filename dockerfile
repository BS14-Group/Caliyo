FROM python:3.10

WORKDIR /
COPY . .

RUN pip install psutil time telegram

ENTRYPOINT ["python"]
CMD ["-u","main.py"]

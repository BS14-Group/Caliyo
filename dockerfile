FROM python:3.10

WORKDIR /
COPY . .

RUN pip install psutil python-telegram-bot

ENTRYPOINT ["python"]
CMD ["-u","main.py"]

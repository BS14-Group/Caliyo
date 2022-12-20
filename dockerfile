# Base image
FROM python:3.10

# Set working directory
WORKDIR /

# Copy all files to working directory
COPY . .

# Install psutil package
RUN pip install psutil python-telegram-bot

# Set command to run when container starts
ENTRYPOINT ["python"]

# Default arguments for command.
CMD ["-u","main.py"]

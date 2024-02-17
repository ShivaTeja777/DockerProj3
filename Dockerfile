# Using lightweight Python 3.9 slim image for efficiency
FROM python:3.9-slim

# Installing necessary packages
RUN apt-get update && apt-get install -y bash

# Setting the working directory inside the container
WORKDIR /home

# Copying the Python script and text files into the container
COPY word_count.py /home/word_count.py
COPY IF.txt /home/data/IF.txt
COPY Limerick-1.txt /home/data/Limerick-1.txt

# Creating the output directory
RUN mkdir -p /home/output

# Running the Python script
CMD ["python", "/home/word_count.py"]

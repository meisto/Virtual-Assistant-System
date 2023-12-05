FROM python:3.13.0a2-bookworm

WORKDIR /usr/src/app

# Copy requirements seperately as to not download image each time
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

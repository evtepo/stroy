FROM python:3.10-slim

WORKDIR /tests

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY utils/docker/launch.sh launch.sh
COPY utils/docker/wait-for-it.sh wait-for-it.sh

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r requirements.txt --no-cache-dir \
    && chmod +x launch.sh \
    && chmod +x wait-for-it.sh

COPY . .

ENTRYPOINT ["sh", "launch.sh"]

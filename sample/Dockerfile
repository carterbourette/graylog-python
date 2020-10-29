FROM python:3.8.3-alpine3.11

RUN apk add --upgrade \
    tzdata \
    && rm -rf /var/cache/apk/*

ENV TZ America/Toronto

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY sample ./sample

ENTRYPOINT [ "python" ] 
CMD [ "-m", "sample.main" ]

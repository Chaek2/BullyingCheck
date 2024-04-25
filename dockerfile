FROM python:3.10-alpine
RUN apk add curl gcc g++ git openssl-dev krb5-dev linux-headers make freetds-dev
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list

RUN mkdir -p /tmp
COPY /src   /app

EXPOSE 5062

CMD [ "python","/app/main.py" ]
FROM python:3.8

WORKDIR /root

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080 

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait

CMD /wait && python3 -u server.py

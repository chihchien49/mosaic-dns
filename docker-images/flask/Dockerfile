FROM tiangolo/uwsgi-nginx-flask:python3.8

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN apt update && apt install dnsutils  -y

RUN mkdir /opt/log



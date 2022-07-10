from locustio/locust:latest

WORKDIR /opt/falcon

COPY requirements.txt /opt/falcon

RUN pip3 install -r requirements.txt

COPY load_tests /opt/falcon/load_tests


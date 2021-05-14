FROM python:3.9.5-buster

WORKDIR /Binance

# RUN apt-get update &&\
#     apt-get install git

COPY requirements.txt /Binance/

RUN pip install -r /Binance/requirements.txt

COPY . /Binance/

# CMD ['/bin/bash']

ENTRYPOINT ["tail", "-f", "/dev/null"]
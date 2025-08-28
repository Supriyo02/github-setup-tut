FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# installing curl
RUN apt-get install -y curl

COPY . .

EXPOSE 8000

CMD [ "python3", "runserver.py"]
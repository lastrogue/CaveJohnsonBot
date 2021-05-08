#Dockerfile, Image, Container
FROM python:3.9

ADD CaveJohnson.py .
ADD .env .

RUN pip install discord.py python-dotenv

CMD [ "python", "./CaveJohnson.py"]
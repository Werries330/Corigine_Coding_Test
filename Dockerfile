FROM python:3

ADD Werner_Mostert.py /
ADD README.txt /

RUN pip install numpy
RUN pip install argparse

CMD [ "python", "-c", "./Werner_Mostert.py", "10"]
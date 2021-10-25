FROM python:3

WORKDIR https://github.com/Werries330/Corigine_Coding_Test

ADD ./Werner_Mostert.py .
ADD ./README.txt .

RUN pip install numpy
RUN pip install --upgrade pip
RUN pip install argparse

ENTRYPOINT [ "python", "./Werner_Mostert.py" ]
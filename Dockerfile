FROM python:3.9.5
ENV PYTHONUNBUFFERED 1
WORKDIR /proyecto
COPY requirements.txt /proyecto/requirements.txt
RUN pip install -r requirements.txt
COPY . /proyecto

CMD python ./proyecto/manage.py runserver 0.0.0.0:8787
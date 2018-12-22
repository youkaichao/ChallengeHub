FROM python:3.6
COPY . /code
ENV DJANGO_CONFIG_PATH /config/django/config.json
WORKDIR /code
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
RUN pip install uwsgi
EXPOSE 80
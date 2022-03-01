FROM python:3.7

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app


RUN apt-get update
RUN apt-get install -y nginx vim default-mysql-server default-libmysqlclient-dev libgl1-mesa-glx
RUN apt-get clean && \
    apt-get autoremove

RUN pip install -r requirements.txt

COPY . /app

RUN /bin/cp -f /app/nginx_website.conf /etc/nginx/sites-available/default
RUN mkdir /var/log/uwsgi && touch /var/log/uwsgi/uwsgi.log

#CMD ["gunicorn", "-k", "gevent", "-b", "0.0.0.0:9000", "app:app"]

#CMD ["service", "nginx", "start"]

#CMD service nginx start ; python3 App.py
#CMD service nginx start ; service redis-server start ; uwsgi --ini /app/uwsgi.ini

CMD ["/bin/bash", "-c", "source /app/run.sh"]
# CMD ["python3", "/app/run.py"]

#CMD /bin/bash

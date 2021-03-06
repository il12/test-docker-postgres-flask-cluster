FROM python:3

COPY ./app /app
WORKDIR /app
RUN pip install -r /app/requirements.txt

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["flaskapp.py"]

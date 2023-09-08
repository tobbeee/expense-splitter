FROM python:3
ADD app.py /
ADD expense_splitter.py /
COPY templates /templates
RUN pip install flask
RUN pip install gunicorn
EXPOSE 8080
CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "app:app" ]

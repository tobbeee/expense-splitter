FROM python:3
ADD app.py /
ADD expense_splitter.py /
RUN pip install flask
RUN pip install gunicorn
EXPOSE 80
CMD [ "gunicorn", "--bind", "0.0.0.0:80", "app:app" ]

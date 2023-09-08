FROM python:3
ADD app.py /
ADD expense_splitter.py /
RUN pip install flask
RUN pip install gunicorn
EXPOSE 8080
CMD [ "gunicorn", "--bind", "4.180.199.250:8080", "app:app" ]

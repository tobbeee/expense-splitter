FROM python:3
ADD app.py /
ADD expense_splitter.py /
RUN pip install flask
CMD [ "python", "./app.py" ]

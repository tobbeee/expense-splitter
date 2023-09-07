FROM python:3
ADD expense_splitter.py /
CMD [ "python", "./expense_splitter.py" ]
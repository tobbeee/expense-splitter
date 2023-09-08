from flask import Flask, render_template, request, redirect, url_for
from expense_splitter import ExpenseSplitter

app = Flask(__name__)
expense_splitter = ExpenseSplitter()

@app.route('/')
def index():
    participants = expense_splitter.participants
    expenses = expense_splitter.expenses
    return render_template('index.html', participants=participants, expenses=expenses)

@app.route('/add_participant', methods=['POST'])
def add_participant():
    name = request.form['participant_name']
    expense_splitter.add_participant(name)
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    description = request.form['expense_description']
    amount = float(request.form['expense_amount'])
    payer = request.form['expense_payer']
    participants = request.form.getlist('expense_participants')
    
    expense_splitter.add_expense(description, amount, payer, participants)
    return redirect(url_for('index'))

@app.route('/compute_owed_amount', methods=['POST'])
def compute_owed_amount():
    expense_splitter.compute_owed_amount()
    expense_splitter.expenses = []
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset_all():
    # Clear all data
    expense_splitter.participants = {}
    expense_splitter.expenses = []

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='4.180.199.250', port=8080, debug=True)

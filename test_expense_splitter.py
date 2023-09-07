import pytest
from expense_splitter import ExpenseSplitter

@pytest.fixture
def expense_splitter():
    return ExpenseSplitter()

def test_add_participant(expense_splitter):
    expense_splitter.add_participant("Tobias")
    assert "Tobias" in expense_splitter.participants

def test_add_expense(expense_splitter):
    expense_splitter.add_participant("Tobias")
    expense_splitter.add_participant("Philip")
    expense_splitter.add_participant("Carl")

    expense_splitter.add_expense("Lasergame", 600, "Tobias", ["Tobias", "Philip", "Carl"])
    assert len(expense_splitter.expenses) == 1

def test_compute_owed_amount(expense_splitter):
    expense_splitter.add_participant("Tobias")
    expense_splitter.add_participant("Philip")
    expense_splitter.add_participant("Carl")

    expense_splitter.add_expense("Lasergame", 600, "Tobias", ["Tobias", "Philip", "Carl"])
    expense_splitter.add_expense("Dinner", 500, "Philip", ["Philip", "Carl"])

    expense_splitter.compute_owed_amount()
    
    # Check if participants owe the correct amounts
    assert expense_splitter.participants["Tobias"] == 0.0
    assert expense_splitter.participants["Philip"] == 200.0
    assert expense_splitter.participants["Carl"] == 450.0

if __name__ == "__main__":
    pytest.main()
import pytest
from flask import url_for
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Expense Splitter" in response.data

def test_add_participant_route(client):
    response = client.post('/add_participant', data={'participant_name': 'Tobias'})
    assert response.status_code == 302  # Redirects to index
    response = client.get('/')
    assert b"Tobias" in response.data

def test_add_expense_route(client):
    client.post('/add_participant', data={'participant_name': 'Tobias'})
    response = client.post('/add_expense', data={
        'expense_description': 'Dinner',
        'expense_amount': 50.0,
        'expense_payer': 'Tobias',
        'expense_participants': ['Tobias'],
    })
    assert response.status_code == 302 
    response = client.get('/')
    assert b"Dinner" in response.data
    assert b"50.0" in response.data

def test_compute_owed_amount_route(client):
    client.post('/add_participant', data={'participant_name': 'Tobias'})
    client.post('/add_expense', data={
        'expense_description': 'Lunch',
        'expense_amount': 20.0,
        'expense_payer': 'Tobias',
        'expense_participants': ['Tobias'],
    })
    response = client.post('/compute_owed_amount')
    assert response.status_code == 302  # Redirects to index
    response = client.get('/')
    assert b"0.0" in response.data  # Assuming owed amount is displayed

def test_reset_all_route(client):
    client.post('/add_participant', data={'participant_name': 'Philip'})
    client.post('/add_expense', data={
        'expense_description': 'Coffee',
        'expense_amount': 10.0,
        'expense_payer': 'Philip',
        'expense_participants': ['Philip', 'Anna'],
    })
    response = client.post('/reset')
    assert response.status_code == 302
    response = client.get('/')
    assert b"Philip" not in response.data  # Participant should be removed
    assert b"Anna" not in response.data # Participant should be removed
    assert b"Coffee" not in response.data  # Expense should be removed

if __name__ == "__main__":
    pytest.main()
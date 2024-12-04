from bank_account import BankAccount
from pytest import fixture

@fixture
def bank_account():
    balance = 100
    account = BankAccount(balance)
    return account

def test_bank_account_balance(bank_account):
    assert bank_account.balance == 100

def test_deposit(bank_account):
    bank_account.deposit(50)     
    assert bank_account.balance == 150    
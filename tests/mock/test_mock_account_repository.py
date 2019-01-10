import pytest

from account_service.api.accounts import AccountNotFound
from account_service.domain.account import Account


def test_store_sets_the_account_number(account_repository):
    account = Account(customer_id='12345', account_status='active')
    account_repository.store(account)

    assert account.account_number is not None


def test_store_generates_a_new_account_number_each_time(account_repository):
    account1 = Account(customer_id='12345', account_status='active')
    account2 = Account(customer_id='12345', account_status='active')
    account_repository.store(account1)
    account_repository.store(account2)

    assert account1.account_number != account2.account_number


def test_fetch_by_account_number_raises_if_not_found(account_repository):
    with pytest.raises(AccountNotFound):
        account_repository.fetch_by_account_number('12345678')


def test_fetch_by_account_number_returns_the_account(account_repository):
    account1 = Account(customer_id='12345', account_status='active')
    account2 = Account(customer_id='99999', account_status='active')
    account_repository.store(account1)
    account_repository.store(account2)

    fetched_account = account_repository.fetch_by_account_number(account1.account_number)

    assert fetched_account is account1

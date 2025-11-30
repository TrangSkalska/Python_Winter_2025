from datetime import datetime
from enum import Enum

class Customer:
    last_id = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Cust[{self.id}, {self.first_name}, {self.last_name}]'

class TransactionType(Enum):
    DEPOSIT = 'DEPOSIT'
    CHARGE = 'CHARGE'
    TRANSFER_IN = 'TRANSFER_IN'
    TRANSFER_OUT = 'TRANSFER_OUT'
    INTEREST = 'INTEREST'

class AccountTransaction:
    def __init__(self, account_id, tx_type, amount, balance_after, description=''):
        self.account_id = account_id
        self.tx_type = tx_type
        self.amount = amount
        self.balance_after = balance_after
        self.description = description
        self.timestamp = datetime.now()  # exact date and time

    def __repr__(self):
        return (f'Tx[{self.timestamp}, acc={self.account_id}, '
                f'{self.tx_type.value}, amount={self.amount}, '
                f'balance_after={self.balance_after}, "{self.description}"]')

class Account:
    last_id = 1000
    yearly_interest_rate = 0.02

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0
        self.transactions = []  # list of AccountTransaction

    def _add_transaction(self, tx_type, amount, description=''):
        tx = AccountTransaction(
            account_id=self.id,
            tx_type=tx_type,
            amount=amount,
            balance_after=self._balance,
            description=description
        )
        self.transactions.append(tx)

    def apply_daily_interest(self):
        # no interest on zero/negative balances
        if self._balance <= 0:
            return
        daily_rate = Account.yearly_interest_rate / 365.0
        interest = self._balance * daily_rate
        self._balance += interest
        self._add_transaction(TransactionType.INTEREST, interest, 'Daily interest')

    def deposit(self, amount):
        # amount must be a number
        if not isinstance(amount, (int, float)):
            raise InvalidAmountException(f'Amount must be a number, got: {amount}')
        # amount must be strictly positive
        if amount <= 0:
            raise InvalidAmountException(f'Invalid amount to deposit: {amount}')
        self._balance += amount
        self._add_transaction(TransactionType.DEPOSIT, amount, 'Deposit')


    def charge(self, amount):
        # amount must be a number
        if not isinstance(amount, (int, float)):
            raise InvalidAmountException(f'Amount must be a number, got: {amount}')
        # amount must be strictly positive
        if amount <= 0:
            raise InvalidAmountException(f'Invalid amount to charge: {amount}')
        # no overdraft: cannot charge more than current balance
        if amount > self._balance:
            raise InsufficientFundsException(
                f'Insufficient funds: tried to charge {amount}, balance {self._balance}'
            )
        self._balance -= amount
        self._add_transaction(TransactionType.CHARGE, -amount, 'Charge')

    def __repr__(self):
        return f'Acc[{self.id}, {self.customer.last_name}, {self._balance}]'

class Bank:
    def __init__(self, name):
        self.name = name
        self.customer_list = []
        self.account_list = []

    def create_customer(self, first_name, last_name):
        c = Customer(first_name, last_name)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def transfer_money(self, from_account_id, to_account_id, amount):
        if not isinstance(amount, (int, float)):
            raise InvalidAmountException(f'Amount must be a number, got: {amount}')
        if amount <= 0:
            raise InvalidAmountException(f'Invalid transfer amount: {amount}')
        if from_account_id == to_account_id:
            raise BankException('Cannot transfer to the same account')

            # find from and to accounts by id
        from_acc = None
        to_acc = None
        for acc in self.account_list:
            if acc.id == from_account_id:
                from_acc = acc
            if acc.id == to_account_id:
                to_acc = acc

        if from_acc is None:
            raise BankException(f'From account with id {from_account_id} not found')
        if to_acc is None:
            raise BankException(f'To account with id {to_account_id} not found')

        from_acc.charge(amount)  # can raise InsufficientFundsException
        to_acc.deposit(amount)

    def run_daily_interest_updater(self):
        for acc in self.account_list:
            acc.apply_daily_interest()

    def __repr__(self):
        return f'Bank[{self.name}: \n{self.customer_list}\n{self.account_list}]'

class BankException(Exception):
    pass

class InsufficientFundsException(BankException):
    pass

class InvalidAmountException(BankException):
    pass

if __name__ == '__main__':
    # create bank and first customer
    bank = Bank('SGH Bank')
    c1 = bank.create_customer('John', 'Smith')

    # create two accounts for this customer
    a1 = bank.create_account(c1)
    a2 = bank.create_account(c1)

    # demo: deposit, transfer and daily interest
    a1.deposit(1000)
    bank.transfer_money(a1.id, a2.id, 300)
    bank.run_daily_interest_updater()

    print(bank)

    # demo: print full transaction history for each account
    print('--- Transactions for a1 ---')
    for tx in a1.transactions:
        print(tx)

    print('--- Transactions for a2 ---')
    for tx in a2.transactions:
        print(tx)

    # demo: show validation and custom exceptions
    try:
        a1.deposit(-500)
        a1.charge(300)
    except InsufficientFundsException as ife:
        print(ife)
    except InvalidAmountException as iae:
        print(iae)

    # demo: create extra accounts and second customer
    a2 = bank.create_account(c1)
    print(bank)
    c2 = bank.create_customer('Anne', 'Brown')
    a3 = bank.create_account(c2)
    print('--------------')
    print(bank)


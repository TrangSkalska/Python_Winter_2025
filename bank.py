class Customer:
    last_id = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Cust[{self.id}, {self.first_name}, {self.last_name}]'

class Account:
    last_id = 1000
    yearly_interest_rate = 0.02  # TODO - will be used to update the interest rate

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        #TODO - as part of the home assignment please extend this method
        if amount <= 0:
            print('Invalid amount.')
            raise InvalidAmountException(f'Invalid amount: {amount}')
        else:
            self._balance += amount

    def charge(self, amount):
        #TODO - as part of the home assignment please extend this method
        if amount > self._balance:
            print('Insufficient funds.')
            raise InsufficientFundsException(f'Insufficient funds: {amount}')
        else:
            self._balance -= amount

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
        # TODO - as part of the home assignment please implement this method - as names suggest the input parameters are
        # ids of the accounts to transfer money from and to and amount to transfer. You may need a helper method to find
        # those accounts based on their ids.
        pass

    def run_daily_interest_updater(self):
        # TODO - as part of the home assignment please implement this method
        pass

    def __repr__(self):
        return f'Bank[{self.name}: \n{self.customer_list}\n{self.account_list}]'

class BankException(Exception):
    pass

class InsufficientFundsException(BankException):
    pass

class InvalidAmountException(BankException):
    pass


if __name__ == '__main__':
    bank = Bank('')


bank = Bank('SGH Bank')

c1 = bank.create_customer('John', 'Smith')
a1 = bank.create_account(c1)

try:
    #a = 500
    #s = 'avcv' + a
    a1.deposit(-500)
    a1.charge(300)
except InsufficientFundsException as ife:
    print(ife)
except InvalidAmountException as iae:
    print(iae)
# except Exception as e:
#     print(e)

a2 = bank.create_account(c1)
print(bank)
c2 = bank.create_customer('Anne', 'Brown')
a3 = bank.create_account(c2)
print('--------------')
print(bank)

#TODO:
# Add deposit and charge method to account - they should have a
# parameter: amount
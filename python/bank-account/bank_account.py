import threading

ACTIVE = "active"
CLOSED = "closed"


class BankAccount(object):
    def __init__(self):
        self.status = CLOSED
        self.balance = 0
        self.lock = threading.Lock()

    def get_balance(self):
        with self.lock:
            if self.status != ACTIVE:
                raise ValueError("Can't query a closed account")
            else:
                return self.balance

    def open(self):
        with self.lock:
            if self.status == ACTIVE:
                raise ValueError("Can't open an already open account")
            else:
                self.status = ACTIVE

    def deposit(self, amount):
        with self.lock:
            if self.status == ACTIVE:
                if amount < 0:
                    raise ValueError("Deposit can't be negative")
                self.balance += amount
            elif self.status == CLOSED:
                raise ValueError("Can't deposit into a closed account")

    def withdraw(self, amount):
        with self.lock:
            if amount < 0:
                raise ValueError("Can't withdraw a negative amount")

            if self.status == ACTIVE:
                if self.balance < amount:
                    raise ValueError("Can't withdraw more than balance")
                else:
                    self.balance -= amount
            elif self.status == CLOSED:
                raise ValueError("Closed account")

    def close(self):
        with self.lock:
            if self.status == CLOSED:
                raise ValueError("Can't close an already closed account")
            else:
                self.balance = 0
                self.status = CLOSED

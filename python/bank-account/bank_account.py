import threading
import time

ACTIVE = "active"
CLOSED = "closed"
PROCESSING = "processing"
SLEEP = 1


class BankAccount(object):
    def __init__(self):
        self.status = CLOSED
        self.balance = 0
        self.lock = threading.Lock()

    def get_balance(self):
        if self.status != ACTIVE:
            raise ValueError("Can't query a closed account")
        else:
            return self.balance

    def open(self):
        if self.status == ACTIVE:
            raise ValueError("Can't open an already open account")
        else:
            self.status = ACTIVE

    def deposit(self, amount):
        if self.status == ACTIVE:
            if self.status == PROCESSING:
                while True:
                    time.sleep(SLEEP ** 2)
                    if self.status == ACTIVE:
                        self.status = PROCESSING
                        break
            if amount < 0:
                raise ValueError("Deposit can't be negative")
            self.balance += amount
            self.status = ACTIVE
        elif self.status == CLOSED:
            raise ValueError("Can't deposit into a closed account")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Can't withdraw a negative amount")

        if self.status == ACTIVE:
            if self.status == PROCESSING:
                while True:
                    time.sleep(SLEEP ** 2)
                    if self.status == ACTIVE:
                        self.status = PROCESSING
                        break
            if self.balance < amount:
                raise ValueError("Can't withdraw more than balance")
            else:
                self.balance -= amount
                self.status = ACTIVE
        elif self.status == CLOSED:
            raise ValueError("Closed account")

    def close(self):
        if self.status == CLOSED:
            raise ValueError("Can't close an already closed account")
        else:
            self.balance = 0
            self.status = CLOSED

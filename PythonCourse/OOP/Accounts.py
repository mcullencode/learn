#encapsulation: main idea is that objects contain the data and the methods that operate on that data, and dont expose the actual implementation.
#OOP isnt the only way to achieve this.

import datetime
import pytz


class Account:
    """Simple account class with balance"""

    #static method. self parameter isnt being used in this method. pycharm suggests that this can be static method

    @staticmethod
    #suggesting that the method should not be used outside of the Accounts class
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        print("Account created for " + self._name)
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("You are poor")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)

    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(2000)
    tim.show_transactions()

    steph = Account("Steph", 800)

    #need to prevent users from being able to alter balance
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()

#rule is attributes starting with a single underscore are for internal use only.
#if you use __balance, then the balance isnt changed by steph.__balance = 200.
#this is due to mangling.

    #check dict to see whats happening
    print(steph.__dict__)
    steph._Account__balance = 40
    steph.show_balance()
    #steph._Account__balance is used, the balance is actually updated. so the double underscore is intended to stop accidental
    #usage, where there shouldnt be meddling. its sort of creating weak  private access


class CashDesk():

    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, taked_money):
        self.taked_money = taked_money
        self.money.update(taked_money)

    def total(self):
        self.total_amount = 0
        for element in self.money:
            self.total_amount += self.money[element] * element
        return self.total_amount

    def can_withdraw_money(self, amount_of_money):
        for element in self.money:
            if self.money[element] != 0:
                if amount_of_money - element > 0:
                    self.money.update({element: self.money[element] - 1})
                    amount_of_money -= element
        return amount_of_money == 0
            
                                    

my_cash_desk = CashDesk()
print(my_cash_desk.money)
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
print(my_cash_desk.money)
print(my_cash_desk.total())
print(my_cash_desk.can_withdraw_money(1))


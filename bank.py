from product.src import *


class Bank:
    def __init__(self, interest_rate):
        self.interest_rate = interest_rate
        self.time = 0
        self.user =


    def show_total_funding(self):
        print(self.total_funding)

    def date_update(self, num=0):
        self.time += 1
        for keys in self.fund:
            value = self.fund.get(keys)
            if num > 1:
                self.fund[keys] = value * (1 + self.interest_rate)**num
            else:
                self.fund[keys] = value * (1 + self.interest_rate)
        self.total_funding = sum(list(self.fund.values()))

    def show_fund(self):
        print(self.fund)




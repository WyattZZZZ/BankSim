import yaml


class Deposit:
    def __init__(self, product_name):
        with open(f'product/yaml/{product_name}.yaml', 'r') as file:
            data = yaml.load(file)
        self.interest_rate = data['interest_rate']
        self.term = data['term']
        self.min_amount = data['min_amount']
        self.max_amount = data['max_amount']
        self.fixed = data['fixed']
        self.time = 0
        self.fund = {}
        self.total_funding = sum(list(self.fund.values()))

    def date_update(self, date):
        self.time += date
        for keys in self.fund:
            value = self.fund.get(keys)
            if date > 1:
                self.fund[keys] = value * (1 + self.interest_rate) ** date
            else:
                self.fund[keys] = value * (1 + self.interest_rate)
        self.total_funding = sum(list(self.fund.values()))

    def fund_update(self, name: str, amount: float):
        if self.fixed:
            if not name in self.fund.keys():
                self.fund.update({name: amount})
            else:
                print("you have been in a fixed deposit")
        else:
            if name in self.fund.keys():
                value = float(self.fund.get(name))
                self.fund.update({name: value + amount})
            else:
                self.fund.update({name: amount})

    def set_time(self, date):
        self.time += date



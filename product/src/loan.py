import yaml


class Loan:
    def __init__(self, product_name):
        with open(f'product/yaml/{product_name}.yaml', 'r') as file:
            data = yaml.load(file)
        self.interest_rate = data['interest_rate']
        self.term = data['term']
        self.min_amount = data['min_amount']
        self.max_amount = data['max_amount']
        self.amount = data['amount']
        self.fixed = data['fixed']
        self.mortgage = data['mortgage']
        self.time = 0
        self.loan = {}
        self.total_loan = sum(list(self.loan.values()))

    async def date_update(self, date):
        self.time += date
        for keys in self.loan:
            value = self.loan.get(keys)
            if date > 1:
                self.loan[keys] = value * (1 + self.interest_rate) ** date
            else:
                self.loan[keys] = value * (1 + self.interest_rate)
        self.total_loan = sum(list(self.loan.values()))

    async def loan_update(self, name: str, amount: float):
        if self.fixed:
            if not name in self.loan.keys():
                self.loan.update({name: amount})
            else:
                print("you have been in a fixed deposit")
        else:
            if name in self.loan.keys():
                value = float(self.loan.get(name))
                self.loan.update({name: value + amount})
            else:
                self.loan.update({name: amount})

    def set_time(self, date):
        self.time += date



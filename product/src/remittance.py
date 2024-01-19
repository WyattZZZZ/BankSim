import yaml

class Remittance:
    def __init__(self, user):
        with open(f'product/yaml/remittance.yaml', 'r') as file:
            data = yaml.load(file)
        self.amount = data['amount']
        self.premium = data['premium']
        self.user = user
        self.time = 0

    def remittance_out(self, target, amount):


    def set_time(self, date):
        self.time += date

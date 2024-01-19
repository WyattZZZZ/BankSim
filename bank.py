from product.src import deposit, loan, remittance
import yaml


class Bank:
    def __init__(self, interest_rate):
        self.interest_rate = interest_rate
        self.time = 0
        self.user = {}
        self.loan_ls = {}
        self.deposit_ls = {}
        self.deposit_node = deposit.Deposit('deposit1')
        self.loan_node = loan.Loan('loan1')

    def creat_account(self, name):
        self.user.update({name: {"deposit": False, "loan": False}})
        with open('user/usr_ls.yaml', 'w') as file:
            yaml.dump(self.user, file, default_flow_style=False)


    def choose_service(self, name, service_type):
        if service_type == "deposit":
            self.user[name["deposit"]] = True
            self.deposit_ls.update({name: 0})
            with open('user/deposit_ls.yaml', 'w') as file:
                yaml.dump(self.deposit_ls, file, default_flow_style=False)
        elif service_type == "loan":
            self.user[name["loan"]] = True
            self.loan_ls.update({name: 0})
            with open('user/loan_ls.yaml', 'w') as file:
                yaml.dump(self.loan_ls, file, default_flow_style=False)
        with open('user/usr_ls.yaml', 'w') as file:
            yaml.dump(self.user, file, default_flow_style=False)


    def date_update(self, num=1):
        self.time += num
        self.deposit_node.date_update(num)
        self.loan_node.date_update(num)

    async def remittance_out(self, target, user, amount):
        self.deposit_node.fund[user] -= amount
        if self.deposit_node.fund[user] < 0:
            print("????")
            self.deposit_node.fund[user] += amount
        else:
            await target.remittance_in(user, amount)

    async def remittance_in(self, user, amount):
        self.deposit_node.fund[user] += amount


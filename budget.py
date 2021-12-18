class Category:

    funds: int
    ledger = []
    count = 0

    def __init__(self, name, funds=0):
        self.funds = funds
        self.name = name

    def deposit(self, amount, description=""):
        self.funds += amount
        Category.ledger.append({"amount": self.funds, "description": description})
        Category.count += 1

    def withdraw(self, amount, description=""):
        if amount <= self.funds:
            self.funds -= amount
            Category.ledger.append({"amount": (-amount), "description": description})
            Category.count += 1
            return True
        return False


def create_spend_chart(categories):
    pass

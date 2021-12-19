class Category:

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

    def get_balance(self):
        return self.funds

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False


def create_spend_chart(categories):
    pass


if __name__ == '__main__':
    food = Category('food')
    clothing = Category('clothing')
    food.deposit(1500, "deposito inicial")
    print(Category.ledger)
    food.withdraw(300, 'Comida do mês')
    print(Category.ledger)
    print(food.get_balance())
    food.transfer(300, clothing)
    print(Category.ledger)
    print(clothing.get_balance())

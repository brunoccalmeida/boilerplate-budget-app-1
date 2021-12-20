class Category:



    def __init__(self, name, funds=0):
        self.funds = funds
        self.name = name
        self.ledger = []
    def __str__(self):
        fh = open("list_of_elements.txt", "w+")
        for element in self.ledger:
            if len(element["description"]) > 23:
                element["description"] = element["description"][0:23]
            fh.write(f'{element["description"]:<23}{element["amount"]:>7}\n')
        fh.write('\n')
        fh.close()
        with open("list_of_elements.txt", "r+") as fh:
            return f'{self.name:*^30}\n{fh.read()}'

    def deposit(self, amount, description=""):
        self.funds += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.funds -= amount
            self.ledger.append({"amount": (-amount), "description": description})
            return True
        return False

    def get_balance(self):
        return self.funds

    def check_funds(self, amount):
        if self.funds >= amount:
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False


def create_spend_chart(categories):
    pass


if __name__ == '__main__':
    food = Category('Food')
    clothing = Category('Clothing')
    food.deposit(1000, 'deposito inicial')
    food.deposit(900, 'deposito')
    food.withdraw(300, 'comida do mes de fevereiro de 2004 no natal')
    food.transfer(100, clothing)
    print(food)


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
            fh.write(f'{element["description"]:<23}{element["amount"]:>7.2f}\n')
        fh.write(f'Total: {self.funds}')
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
    list_of_categories = categories
    number_of_categories = len(list_of_categories)
    dict_of_variables = {}
    for n in range(1, number_of_categories+1):
        dict_of_variables[f'cat{n}'] = 0
    for category in list_of_categories:
        print(category.__repr__())




    #         if cat.name == 'Food' and element['amount'] < 0:
    #             food_total_spent += element['amount']
    #         if cat.name == 'Clothing' and element['amount'] < 0:
    #             clothing_total_spent += element['amount']
    #         if cat.name == 'Entertainment' and element['amount'] < 0:
    #             entertainment_total_spent += element['amount']
    # total = food_total_spent + clothing_total_spent + entertainment_total_spent
    # food_percent = (food_total_spent / total) * 100
    # clothing_percent = (clothing_total_spent / total) * 100
    # entertainment_percent = (entertainment_total_spent / total) * 100
    # print(f'Food: {food_percent:.0f} Clothing: {clothing_percent:.0f} Entertainment: {entertainment_percent:.0f}')


if __name__ == '__main__':
    food = Category('Food', funds=1000)
    clothing = Category('Clothing', funds=1000)
    entertainment = Category('Entertainment', funds=1000)
    food.withdraw(20, 'groceries')
    food.withdraw(50, 'icecream')
    food.withdraw(100, 'chocolate')
    food.deposit(10)
    clothing.withdraw(50, 'T-shirt')
    clothing.withdraw(80, 'sockes and underware')
    clothing.withdraw(30, 'gloves')
    clothing.withdraw(90, 'trousers')
    clothing.deposit(80)
    entertainment.withdraw(100, 'movies')
    entertainment.withdraw(90, 'pc game')
    entertainment.deposit(50)
    cat_list = [food, clothing, entertainment]
    create_spend_chart(cat_list)

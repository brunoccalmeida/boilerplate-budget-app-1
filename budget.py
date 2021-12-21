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
    count = 0

    for n in range(number_of_categories):
        dict_of_variables[f'{list_of_categories[n].name}'] = 0

    for cat in list_of_categories:
        for element in cat.ledger:
            if element['amount'] < 0:
                dict_of_variables[f'{list_of_categories[count].name}'] += element['amount']
        count += 1
    soma = 0

    for v in dict_of_variables.values():
        soma += v
    dict_of_percentages = dict_of_variables.copy()

    for k, v in dict_of_variables.items():
        dict_of_percentages[k] = round((v / soma) * 100)

    names_of_categories = []
    for item in list_of_categories:
        names_of_categories.append(item.name)

    # maior_palavra_categoria = 0
    #
    # for palavra in names_of_categories:
    #     if len(palavra) > maior_palavra_categoria:
    #         maior_palavra_categoria = len(palavra)

    with open('chart.txt', 'w+') as file_chart:
        for i in range(100, 0, -10):
            file_chart.write(f'{i:>3}| ')
            for v in dict_of_percentages.values():
                if i < v:
                    file_chart.write(f'o  ')
            file_chart.write(f'\n')
        file_chart.write(f'    {"":->{len(dict_of_variables)*3+1}}\n')
        for i in names_of_categories:
            file_chart.write(f'{i[0]:}')



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

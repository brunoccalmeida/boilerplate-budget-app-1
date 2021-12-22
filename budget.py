class Category:

    def __init__(self, name, funds=0):
        self.funds = funds
        self.name = name
        self.ledger = []

    def __str__(self):  # This method changes the way of how print(class) works
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

    # Creates a dictionary of categories based on how many are given in the categories list
    for n in range(number_of_categories):
        dict_of_variables[f'{list_of_categories[n].name}'] = 0

    # Finds the withdraws calls of every category by looking at their ledgers and add them to
    # each category on the dictionary that was created above
    for cat in list_of_categories:
        for element in cat.ledger:
            if element['amount'] < 0:
                dict_of_variables[f'{list_of_categories[count].name}'] += element['amount']
        count += 1

    # Gets the total sum of withdraws made
    sum_of_withdraws = 0
    for percentage in dict_of_variables.values():
        sum_of_withdraws += percentage

    # Gets the percentage spent of each category and rounds it up to the nearest 10
    dict_of_percentages = dict_of_variables.copy()
    for k, percentage in dict_of_variables.items():
        dict_of_percentages[k] = round((percentage / sum_of_withdraws) * 100)

    # Saves the values of the percentage spent on each category
    dict_of_percentages_rounded = {}
    for k, v in dict_of_percentages.items():
        dict_of_percentages_rounded[k] = v

    # Makes a list of the names of the categories
    names_of_categories = []
    for item in list_of_categories:
        names_of_categories.append(item.name)

    # Gets the length of the biggest word in all of the categories
    biigest_word_in_categories = 0
    for palavra in names_of_categories:
        if len(palavra) > biigest_word_in_categories:
            biigest_word_in_categories = len(palavra)

    # Make every category word have the same length for them to be printed later
    names_of_categories_same_length = []
    for word in names_of_categories:
        names_of_categories_same_length.append(word.ljust(biigest_word_in_categories))

    # Writes the spend chart as requested
    with open('chart.txt', 'w+') as file_chart:
        file_chart.write(f'Percentage spent by category\n')
        col = 0
        lin = 0
        for i in range(100, -1, -10):
            file_chart.write(f'{i:>3}| ')
            for percentage in dict_of_percentages_rounded.values():
                if percentage >= i:
                    file_chart.write(f'o  ')
                else:
                    file_chart.write(f'   ')
            file_chart.write(f'\n')

        file_chart.write(f'    {"":->{len(dict_of_variables)*3+1}}\n')
        for col in range(biigest_word_in_categories):
            file_chart.write(f'     ')
            for line in range(number_of_categories):
                file_chart.write(f'{names_of_categories_same_length[line][col]}  ')
            file_chart.write('\n')
    with open('chart.txt', 'r+') as file_chart:
        data = file_chart.read().rstrip('\n')
        return data


if __name__ == '__main__':
    food = Category('Food', funds=900)
    business = Category('Business', funds=900)
    entertainment = Category('Entertainment', funds=900)
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    cat_list = [business, food, entertainment]
    create_spend_chart(cat_list)

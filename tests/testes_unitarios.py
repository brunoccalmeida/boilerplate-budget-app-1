import budget


def initialize(category):
    category_name = budget.Category(f"{category}")
    category_name.deposit(1000, "deposito inicial")
    return category_name


def close(name):
    name.funds = 0
    name.ledger.clear()


def test_ledger():
    food = initialize('Food')
    clothing = budget.Category('clothing')
    assert food.ledger[-1] == {"amount": 1000, "description": "deposito inicial"}
    food.withdraw(250, "almoço de ontem")
    assert food.ledger[-1] == {"amount": -250, "description": "almoço de ontem"}
    food.transfer(300, clothing)
    assert food.ledger[-1] == {"amount": -300, "description": "Transfer to clothing"}
    assert clothing.ledger[-1] == {"amount": 300, "description": "Transfer from Food"}
    close(food)


def test_deposit():
    food = initialize('Food')
    assert food.funds == 1000
    food.deposit(2000, "salario do mes")
    assert food.funds == 3000
    close(food)


def test_withdraw():
    food = initialize('Food')
    food.withdraw(250, "almoço de ontem")
    assert food.funds == 750
    assert food.withdraw(1500) is False
    close(food)


def test_get_balance():
    food = initialize('Food')
    assert food.get_balance() == 1000
    food.withdraw(800)
    assert food.get_balance() == 200
    food.withdraw(1000)
    assert food.get_balance() == 200
    food.deposit(300)
    assert food.get_balance() == 500
    close(food)


def test_transfer():
    food = initialize('Food')
    clothing = initialize("Clothing")
    food.transfer(300, clothing)
    assert food.funds == 700
    assert clothing.funds == 1300
    food.transfer(1000, clothing)
    assert food.funds == 700
    assert clothing.funds == 1300
    clothing.funds = 0
    close(food)
    close(clothing)


def test_check_funds():
    food = initialize('Food')
    assert food.check_funds(1200) is False
    assert food.check_funds(1000) is True
    assert food.check_funds(1001) is False
    assert food.check_funds(999) is True
    assert food.check_funds(1) is True
    close(food)


def test_to_string():
    food = initialize('Food')
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    assert str(food) == f"*************Food*************\ndeposito inicial       1000.00\n" \
                        f"groceries               -10.15\nrestaurant and more foo -15.89\nTotal: 973.96"


def test_create_spend_chart():
    food = initialize('Food')
    clothing = initialize('Clothing')
    entertainment = initialize('entertainment')
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


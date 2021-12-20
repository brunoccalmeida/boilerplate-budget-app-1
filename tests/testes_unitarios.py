import budget


def initialize_food():
    food = budget.Category("food")
    food.deposit(1000, "deposito inicial")
    return food


def closing_food(food):
    food.funds = 0
    food.ledger.clear()


def test_ledger():
    food = initialize_food()
    clothing = budget.Category('clothing')
    assert food.ledger[-1] == {"amount": 1000, "description": "deposito inicial"}
    food.withdraw(250, "almoço de ontem")
    assert food.ledger[-1] == {"amount": -250, "description": "almoço de ontem"}
    food.transfer(300, clothing)
    assert food.ledger[-1] == {"amount": -300, "description": "Transfer to clothing"}
    assert clothing.ledger[-1] == {"amount": 300, "description": "Transfer from food"}
    closing_food(food)


def test_deposit():
    food = initialize_food()
    assert food.funds == 1000
    food.deposit(2000, "salario do mes")
    assert food.funds == 3000
    closing_food(food)


def test_withdraw():
    food = initialize_food()
    food.withdraw(250, "almoço de ontem")
    assert food.funds == 750
    assert food.withdraw(1500) is False
    closing_food(food)


def test_get_balance():
    food = initialize_food()
    assert food.get_balance() == 1000
    food.withdraw(800)
    assert food.get_balance() == 200
    food.withdraw(1000)
    assert food.get_balance() == 200
    food.deposit(300)
    assert food.get_balance() == 500
    closing_food(food)


def test_transfer():
    food = initialize_food()
    clothing = budget.Category("clothing")
    clothing.deposit(1000, "deposito inicial")
    food.transfer(300, clothing)
    assert food.funds == 700
    assert clothing.funds == 1300
    food.transfer(1000, clothing)
    assert food.funds == 700
    assert clothing.funds == 1300
    clothing.funds = 0
    closing_food(food)


def test_check_funds():
    food = initialize_food()
    assert food.check_funds(1200) is False
    assert food.check_funds(1000) is True
    assert food.check_funds(1001) is False
    assert food.check_funds(999) is True
    assert food.check_funds(1) is True
    closing_food(food)


def test_to_string():
    food = initialize_food()

import budget


def test_ledger():
    food = budget.Category("food")
    food.deposit(1000, "deposito inicial")
    clothing = budget.Category('clothing')
    assert budget.Category.ledger[budget.Category.count - 1] == {"amount": 1000, "description": "deposito inicial"}
    food.withdraw(250, "almoço de ontem")
    assert budget.Category.ledger[budget.Category.count - 1] == {"amount": -250, "description": "almoço de ontem"}
    food.transfer(300, clothing)
    assert budget.Category.ledger[budget.Category.count - 2] == {"amount": -300, "description": "Transfer to clothing"}
    assert budget.Category.ledger[budget.Category.count - 1] == {"amount": 300, "description": "Transfer from food"}
    food.funds = 0
    budget.Category.count = 0
    budget.Category.ledger.clear()


def test_deposit():
    food = budget.Category("food")
    food.deposit(1000, "deposito inicial")
    assert food.funds == 1000
    food.deposit(2000, "salario do mes")
    assert food.funds == 3000
    food.funds = 0
    budget.Category.count = 0
    budget.Category.ledger.clear()


def test_withdraw():
    food = budget.Category("food")
    food.deposit(1000, "deposito inicial")
    food.withdraw(250, "almoço de ontem")
    assert food.funds == 750
    assert food.withdraw(1500) is False
    food.funds = 0
    budget.Category.count = 0
    budget.Category.ledger.clear()


def test_get_balance():
    food = budget.Category("food")
    food.deposit(1000, "deposito inicial")
    assert food.get_balance() == 1000
    food.withdraw(800)
    assert food.get_balance() == 200
    food.withdraw(1000)
    assert food.get_balance() == 200
    food.deposit(300)
    assert food.get_balance() == 500
    food.funds = 0
    budget.Category.count = 0
    budget.Category.ledger.clear()


def test_transfer():
    food = budget.Category("food")
    food.deposit(1000, "deposito inicial")
    clothing = budget.Category("clothing")
    clothing.deposit(1000, "deposito inicial")
    food.transfer(300, clothing)
    assert food.funds == 700
    assert clothing.funds == 1300
    food.transfer(1000, clothing)
    assert food.funds == 700
    assert clothing.funds == 1300
    food.funds = 0
    clothing.funds = 0
    budget.Category.count = 0
    budget.Category.ledger.clear()


def test_check_funds():
    food = budget.Category("food")
    food.deposit(1000, "deposito inicial")
    assert food.check_funds(1200) is False
    assert food.check_funds(1000) is True
    assert food.check_funds(1001) is False
    assert food.check_funds(999) is True
    assert food.check_funds(1) is True
    food.funds = 0
    budget.Category.count = 0
    budget.Category.ledger.clear()


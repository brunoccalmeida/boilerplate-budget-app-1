import budget


def test_deposit_food():
    food = budget.Category("food")
    food.deposit(1000, "deposito inicial")
    assert budget.Category.ledger[budget.Category.count-1] == {"amount": 1000, "description": "deposito inicial"}
    budget.Category.count = 0
    budget.Category.ledger.clear()


def test_withdraw_food():
    food = budget.Category("food")
    food.deposit(1000, "deposito inicial")
    assert budget.Category.ledger[budget.Category.count - 1] == {"amount": 1000, "description": "deposito inicial"}
    food.withdraw(250, "almoço de ontem")
    assert food.funds == 750
    assert budget.Category.ledger[budget.Category.count - 1] == {"amount": -250, "description": "almoço de ontem"}
    assert food.withdraw(1500) is False
    budget.Category.count = 0
    budget.Category.ledger.clear()



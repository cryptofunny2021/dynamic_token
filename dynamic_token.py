contract DynamicToken:

    def __init__(self):
        self.balances = {}

    def mint(self, user, amount, factor):
        if user not in self.balances:
            self.balances[user] = 0

        adjusted = amount + (factor * 0.1)
        self.balances[user] += adjusted
        return adjusted

    def burn(self, user, amount):
        if self.balances.get(user, 0) >= amount:
            self.balances[user] -= amount
            return True
        return False

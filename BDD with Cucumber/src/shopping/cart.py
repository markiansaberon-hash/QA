class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append((name, price))

    @property
    def total(self):
        return round(sum(price for _, price in self.items), 2)
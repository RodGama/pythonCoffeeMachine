class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, cents, dollars):
        self.cents = cents
        self.dollars = dollars

    def add_money(self, deposit_dollars, deposit_cents):
        if self.cents + deposit_cents >= 100:
            dollars = (self.cents + deposit_cents) // 100
            deposit_dollars += dollars
            self.cents = (self.cents + deposit_cents) % 100
        else:
            self.cents += deposit_cents
        self.dollars += deposit_dollars



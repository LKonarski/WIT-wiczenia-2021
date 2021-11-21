class BankCard():
    def __init__(self, owner, number, provider):
        self.owner = owner
        self.number = number
        self.provider = provider

    def get_owner(self):
        print(get_owner)

    def get_number(self):
        print(get_number)

    def get_provider(self):
        print(get_provider)

class BankAccount():
    def __init__(self, owner, balance, bank):
        self.owner = owner
        self.balance = balance
        self.bank = bank

    def get_owner(self):
        print(get_owner)

    def get_balance(self):
        print(get_balance)

    def get_bank(self):
        print(get_bank)

    def set_balance():
        print(set_balance)

class Bank():
    def __init__(self, name, bank_accounts, bank_cards):
        self.name = name
        self.bank_accounts = bank_accounts
        self.bank_cards = bank_cards

    def get_bank_accounts(self):
        print(get_bank_accounts)

    def get_bank_cards(self):
        print(get_bank_cards)

class CreditCard(BankCard):
    def __init__(self, owner, number, provider, balance, payments_history):
        super().__init__(owner, number, provider)
        self.balance = balance
        self.payments_history = payments_history

    def get_balance(self):
        print(get_balance)

    def set_balance(self):
        print(set_balance)

    def get_payments_history(self):
        print(get_payments_history)

class GoldenCreditCard(CreditCard):
    def __init__(self, owner, number, provider, balance, payments_history, reward_points):
        super.__init__(owner, number, provider, balance, payments_history)
        self.reward_points = reward_points

    def get_reward_points(self):
        print(get_reward_points)

    def set_reward_points(self):
        print(set_reward_points)

class PremiumBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, financial_manager):
        super().__init__(owner, balance, bank)
        self.financial_manager = financial_manager

    def get_financial_manager(self):
        print(get_financial_manager)

    def set_financial_manager(self):
        print(set_financial_manager)

class StudentBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, overdraft_balance, overdraft_limit):
        super().__init__(owner, balance, bank)
        self.overdraft_balance = overdraft_balance
        self.overdraft_limit = overdraft_limit

    def get_overdraft_balance(self):
        print(get_overdraft_balance)

    def set_overdraft_balance(self):
        print(set_overdraft_balance)

    def get_overdraft_limit(self):
        print(get_overdraft_limit)

    def set_overdraft_limit(self):
        print(set_overdraft_limit)

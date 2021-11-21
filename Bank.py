class BankCard:
    def __init__(self, owner, number, provider):
        self.owner = owner
        self.number = number
        self.provider = provider

    def get_number(self):
        print(self.number)

    def get_owner(self):
        print(self.owner)

    def get_provider(self):
        print(self.provider)


class BankAccount:
    def __init__(self, owner, balance, bank):
        self.owner = owner
        self.balance = balance
        self.bank = bank

    def get_owner(self):
        print(self.owner)

    def get_balance(self):
        print(self.balance)

    def get_bank(self):
        print(self.bank)

    def set_balance(self, balance):
        self.balance = balance


class Bank:
    def __init__(self, name, bank_accounts, bank_cards):
        self.name = name
        self.bank_accounts = bank_accounts
        self.bank_cards = bank_cards

    def get_bank_accounts(self):
        print(self.bank_accounts)

    def get_bank_cards(self):
        print(self.bank_cards)


class CreditCard(BankCard):

    def __init__(self, balance, payments_history, owner, number, provider):
        super().__init__(owner, number, provider)
        self.balance = balance
        self.payments_history = payments_history

    def get_balance(self):
        print(self.balance)

    def set_balance(self, balance):
        self.balance = balance

    def get_payments_history(self):
        print(self.payments_history)


class GoldenCreditCard(CreditCard):
    def __init__(self, balance, payments_history, owner, provider, number, reward_points):
        super().__init__(balance, payments_history, owner, number, provider)
        self.reward_points = reward_points

    def get_reward_points(self):
        print(self.reward_points)

    def set_reward_points(self, reward_points):
        self.reward_points = reward_points


class PremiumBankAccount(BankAccount):
    def __init__(self, financial_manager, owner, balance, bank):
        super().__init__(owner, balance, bank)
        self.financial_manager = financial_manager

    def get_financial_manager(self):
        print(self.financial_manager)

    def set_financial_manager(self, financial_manager):
        self.financial_manager = financial_manager


class StudentBankAccount(BankAccount):
    def __init__(self, owner, balance, bank, overdraft_balance, overdraft_limit):
        super().__init__(owner, balance, bank)
        self.overdraft_balance = overdraft_balance
        self.overdraft_limit = overdraft_limit

    def get_overdraft_balance(self):
        print(self.overdraft_balance)

    def set_overdraft_balance(self, overdraft_balance):
        self.overdraft_balance = overdraft_balance

    def get_overdraft_limit(self):
        print(self.overdraft_limit)

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit

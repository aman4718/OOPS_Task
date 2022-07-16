# Multilevel Inheritance
class bank:
    def transaction(self):
        print("Total Transaction Value")
    def account_opening(self):
        print("this will show account open status")
    def deposit(self):
        print("this will share your deposited account")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transaction to icici through hdfc")


class icici(HDFC_bank):
    pass

i =icici()
i.hdfc_to_icici()
i.deposit()
i.account_opening()
i.transaction()
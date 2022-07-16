# multiple Inheritance
class bank:
    def transaction(self):
        print("Total Transaction Value")
    def account_opening(self):
        print("this will show account open status")
    def deposit(self):
        print("this will share your deposited account")

    def test(self):
        print("this is test method from bank")

class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transaction to icici through hdfc")
    def test(self):
        print("this is test methods from hdfc")

class ineron_bank:
    def account_status_icici(self):
        print("print a account status in icici")
class icici(HDFC_bank,bank,ineron_bank):
    def icici_trans(self):
        num = 45+65;
        print(num)

i = icici()
i.account_opening()
i.deposit()
i.transaction()
i.hdfc_to_icici()
i.icici_trans()
i.test()
i.account_status_icici()

### same function in both class then it will depend
### on argument passing in child class if i pass
# bank first as arfument then bank will be first #priority and if give hdfc in first argument then #hdfc will get the priority
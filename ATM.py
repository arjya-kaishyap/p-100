from asyncio.proactor_events import _ProactorBaseWritePipeTransport


class ATM :
    def__init__(self, cardnumber, pin )
        self.cardnumber = cardnumber
        self.pin = pin

    def balenceinquiry(self):
        new_amount = 100-amount
        print("You balence is : $100")

    def cashwidthdrawl(self, amount):
        new_amount = 100-amount
        print("You withdrawed: " + str(amount) + "Tour remaining balance is: " + str(new_amount))

def main():
    name = input("Hello what is your name?")
    print("Hello, " + name)
    cardnumber = input("Insert your card number: ")
    pin = input("Enter your pin: ")
    new_user = Atm(cardnumber, pin)

    print("choose your activity")
    print("1. Balance Inquiry")
    print("2.cash withdrawal")
    activity = init(input("Enter activity choise: "))

    if (activity == 1):
        new_user.balanceinquiry()
    elif (activity == 2):
        amount = init(input("Enter the amount: "))
        new_user.cashwidthdrawal(amount)
    else:
        print("Enter a valid number")

if__name__=="__main__":
    main()
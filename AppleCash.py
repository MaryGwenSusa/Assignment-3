def openStatement():
    print(f"Budget for Comfort Food: Apple")

def cashMonitor():
    yourWallet = float(input('Your Current Money:\n> '))
    return yourWallet

def fluctuationPrice():
    priceOfApple = float(input('How much is the apple?\n> '))
    return priceOfApple

def computation(money, price):
    maximumNumberOfApples = int(money/price)
    remainingMoney = float(money%price)
    return print(f"You can buy {maximumNumberOfApples} and your change is {remainingMoney:.2f}.")

openStatement()
currentMoney = cashMonitor()
currentPrice = fluctuationPrice()
computation(currentMoney, currentPrice)


# another version
def openStatement():
    print(f"Budget for Comfort Food: Apple")

def computation(money, price):
    maximumNumberOfApples = int(money/price)
    remainingMoney = float(money%price)
    return print(f"You can buy {maximumNumberOfApples} and your change is {remainingMoney:.2f}.")

openStatement()
yourWallet = float(input('Your Current Money:\n> '))
priceOfApple = float(input('How much is the apple?\n> '))
computation(yourWallet, priceOfApple)

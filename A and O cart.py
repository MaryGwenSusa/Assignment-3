def welcome():
    print(f"Welcome to Apple and Orange Cart!")

def total():
    def computeAppleQ():
        appleQ = int(input("How many apples do you want to buy?\n> "))
        appleQ*=20
        return appleQ

    def computeOrangeQ():
        orangeQ = int(input("How many oranges do you want to buy?\n> "))
        orangeQ*=25
        return orangeQ
    totalAmount = computeAppleQ()+computeOrangeQ()
    return totalAmount

def calculation(gTotal):
    print(f"The total amount is {gTotal}.")

welcome()
grandTotal = total()
calculation(grandTotal)


# another version
def welcome():
    print(f"Welcome to Apple and Orange Cart!")

def computeAppleQ():
    appleQ = int(input("How many apples do you want to buy?\n> "))
    appleQ*=20
    return appleQ
   
def computeOrangeQ():
    orangeQ = int(input("How many oranges do you want to buy?\n> "))
    orangeQ*=25
    return orangeQ

def calculation(gTotal):
    print(f"The total amount is {gTotal}.")

welcome()
grandTotal = computeAppleQ()+computeOrangeQ()
calculation(grandTotal)


# third version
def welcome():
    print(f"Welcome to Apple and Orange Cart!")

def total():
    def computeAppleQ(appleQ):
        appleQ*=20
        return appleQ
   
    def computeOrangeQ(orangeQ):
        orangeQ*=25
        return orangeQ
    totalAmount = computeAppleQ(appleQ)+computeOrangeQ(orangeQ)
    return totalAmount

def calculation(gTotal):
    print(f"The total amount is {gTotal}.")

welcome()
appleQ = int(input("How many apples do you want to buy?\n> "))
orangeQ = int(input("How many oranges do you want to buy?\n> "))
grandTotal = total()
calculation(grandTotal)
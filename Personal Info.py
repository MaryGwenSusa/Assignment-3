def header():
    print(f"Personal Identification")

def obtainName():
    yourName = input("Name: ")
    return yourName

def obtainAge():
    yourAge = int(input("Age: "))
    return yourAge

def obtainAddress():
    yourAddress = input("Address: ")
    return yourAddress

def intro(nameX, ageX, addressX):
    print (f"Hi, my name is {nameX}. I am {ageX} years old and I live in {addressX}.")

header()
name = obtainName()
age = obtainAge()
address = obtainAddress()
intro(name, age, address)

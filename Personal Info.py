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


# another version
def header():
    print(f"Personal Identification")

def obtainPersonalInfo():
    yourName = input("Name: ")
    yourAge = int(input("Age: "))
    yourAddress = input("Address: ")
    return print (f"Hi, my name is {yourName}. I am {yourAge} years old and I live in {yourAddress}.")

header()
obtainPersonalInfo()

# another version
def header():
    print(f'Personal Information')

def obtainPersonalInfo(name, age, address):
    return print(f'Hi, my name is {name}. I am {age} years old and I live in {address}.')

header()
yourName = input("Name:")
yourAge = int(input("Age:"))
yourAddress = input("Address:")
obtainPersonalInfo(yourName, yourAge, yourAddress)

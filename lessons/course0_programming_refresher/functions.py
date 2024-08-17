from shutil import unregister_archive_format
from turtledemo.penrose import inflatedart


def greetings(name="Oscar", greeting="Have faith"):
    print(greeting, "!", name, sep=" ")


# greetings("Oscar", "Everything will be ok, best times are coming now")

def sqr(a):
    return print(a * a)


def total(*args):
    tot = 0
    for n in args:
        tot += n
    print(tot)


# total(25, 15)

def information(**kwargs):
    for key in kwargs.keys():
        print(key, ":", kwargs[key])


# information(name = "Oscar Garcia", age = 43)


def net_amount(Amount, tax=18, discount=10):
    disc = (Amount * discount / 100)
    tax_amny = (Amount - disc) * tax / 100
    net = (Amount - disc) + tax_amny
    print(round(net, 2))


amnt= float(input('Please enter the bill amount: '))
tax= float(input('Please enter tax: '))
discount = float(input('Please enter discount: '))

return_value = net_amount(amnt, tax, discount)

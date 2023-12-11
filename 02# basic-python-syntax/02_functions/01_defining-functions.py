# 01_defining-functions
def greeting(name):
    print("welcome " + name)


greeting("ahmed")


# Simple and basics function defining

def welcome(welcome):
    Xname = input("What is your name sir ")
    print("welcome sir to the department of Gaza" + Xname)


welcome("")


# Here is a nother example of our def FUnction.

def math(MathX):
    for Number in range(1, 13):
        total = 0
        total += Number
        for total in range(1, 13):
            xtotal = 0
            xtotal += total
            print(xtotal)
        print(total, 'X', xtotal, '=', xtotal * total)

math("")

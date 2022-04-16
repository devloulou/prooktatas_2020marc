# Írjunk  egy nagyon alap számológép programot: egyszerre 2 számmal
# történő műveletek elvégzését fejlesztjük le
# + - * / 
# hibakezelés
# belső függvényekkel

from decimal import DivisionByZero


def calculator(num1, num2, operation):

    def addition():
        return num1 + num2

    def substraction():
        return num1 - num2

    def multiplication():
        return num1 * num2

    def division():
        return num1 / num2

    if '+' == operation:
        return addition()

    elif '-' == operation:
        return substraction()

    elif '*' == operation:
        return multiplication()

    elif '/' == operation:
        if 0 == num2:
            raise DivisionByZero("You try to division with zero")
       
        return division()
    
    else:
        #raise Exception("You try to division with zero")
        #raise DivisionByZero("You try to division with zero")
        raise Exception("Not a valid operation! Please select + - * /!")

eredmeny = calculator(4, 1, '/')

print(eredmeny)

###########################################################################


##########################################################################
def main():
    x = 5
    def inner_func():
        print("inner_func running")

    def inner_func2():
        print("inner_func2 running")

    inner_func()
    inner_func2()

#main()





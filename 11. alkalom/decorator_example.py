
"""
@decorator_neve
def my_func():
    pass


"""

# decorator fogalma: olyan függvény, amely anélkül ad plusz
# funkcionalitást - vagy működést - egy másik függvényhez
# hogy az módosítana rajta


def my_func():
    print("Sziasztok!")

def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

my_func()

printer = start_end_decorator(my_func)

print("##########################")


@start_end_decorator
def my_func():
    print("Ez az első decoratorral megadott függvényem")

my_func()

# mikor célszerű decoratort használni

# Debuggolsz
# Logolsz
# Futási időt mérsz
# Cacheléshez


print("##########################")

def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


@start_end_decorator
def add_5(x):
    return x + 5

print(add_5(10))


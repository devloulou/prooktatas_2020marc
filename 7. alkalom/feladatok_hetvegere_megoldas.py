# 1. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legkisebb értéket ezek közül!
def my_func(a, b, c):
    return min(a, b, c)

print(my_func(1, 2, 3))

def my_func(a, b, c):
    if b > a and c > a:
            return a
    elif a > b and c > b:
        return b
    else:
        return c
print(my_func(1, 2, 3))

print("#####################################")
def my_func():
    a = int(input())
    b = int(input())
    c = int(input())

    return min(a, b, c)

#print(my_func())

#print(my_func(1, 2, 3))

print("#####################################")

# 2. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legnagyobb értéket ezek közül!

def my_func(a, b, c):
    return max(a, b, c)

print(my_func(10, 12, 13))
print("#####################################")
def my_func(a, b, c):
    if b < a and c < a:
            return a
    elif a < b and c < b:
        return b
    else:
        return c

print(my_func(11, 11, 10))
print("#####################################")

# 3. Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
# érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

def my_func(x):
    if x < 50:
        return 1
    elif 50 <= x < 60:
        return 2
    elif 60 <= x < 70:
        return 3
    elif 70 <= x < 85:
        return 4
    else:
        return 5

def my_func(x):
    if x < 50:
        return 1
    elif x < 60:
        return 2
    elif x < 70:
        return 3
    elif x < 85:
        return 4
    else:
        return 5
print("#####################################")

print(my_func(60))

####################################################

# 4. Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
# hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!

def my_func(x):
    # and egy olyan logikai kapcsolat, ahol mind a 2 tagnak igaznak kell lennie
    if x%3==0 and x%5==0:
        return f"A {x} szám 3-al és 5-el is oszthatató "
    else:
        if x%3==0:
            return f"A {x} szám 3-al oszthatató "
        elif x%5==0:
            return f"A {x} szám 5-el oszthatató "
        
        else:
            return f"A {x} szám nem osztható sem 5-el, sem 3-al."

print(my_func(20))

# 5. Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
# hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!
print("#####################################")

def my_func(a, b, c):
    if a + b == c:
        return f"az {a} és {b} -re igaz az állítás. Az első és második szám."
    elif a + c == b:
        return f"az {a} és {c} -re igaz az állítás. Az első és harmadik szám"
    elif b + c == a:
         return f"az {b} és {c} -re igaz az állítás. Második és harmadik szám."
    else:
        return "Egyik számra sem igaz, az állítás"


print(my_func(2, 2, 3))
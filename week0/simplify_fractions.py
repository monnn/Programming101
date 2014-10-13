from fractions import Fraction


def simplify_fractions(fraction):
    fraction = str(fraction)
    array = fraction.split(", ")
    a = array[0]
    a = a.replace('(', '')
    array[0] = a
    a = int(a)
    b = array[1]
    b = b.replace(')', '')
    array[1] = b
    b = int(b)
    print(array)
    return Fraction(a, b)
print(simplify_fractions((63, 462)))

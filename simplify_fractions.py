def simplify_fractions(fraction):
    first = fraction[1]
    second = fraction[2]
    #n = str(fraction)
    #array = n. split(", ")
    #double = {array[1]: array[2]}
    for i in range(2, int(fraction[1])):
        if fraction[1] % i == 0 and fraction[2] % i == 0:
            fraction[1] /= i 
            fraction[2] /= i
        answer = str(fraction[1]) + ", " + str(array[2])
    return answer
print(simplify_fractions(3, 9))
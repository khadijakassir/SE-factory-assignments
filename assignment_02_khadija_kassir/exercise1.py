def number(s):
    factorial = 1
    for i in range (1, s+1):
        factorial *= i
    return factorial   
n = int(input(" give me a number:"))
print (number(n))

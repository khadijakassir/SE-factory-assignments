luckynum_checker = int(input("give me a four digit number to check if it is lucky: "))
digit = luckynum_checker
a= digit // 1000
b = (digit // 100)%10
c = (digit // 10)%10
d = digit % 10
if a+b == c+d:
    print("F")
else: 
    print("U")
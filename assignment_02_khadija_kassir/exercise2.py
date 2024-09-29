def divisors():
  n = int(input("give me a number: "))
#list to store the divisors
  list = []
  for i in range(1, n+1):
    if (n % i == 0): 
      list.append(i)    
  return list
print(divisors())
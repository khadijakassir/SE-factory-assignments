def Even_num():
  integers = []
  n = int(input("how many integers you want: "))
  for i in range(n):
    integer = int(input("what is the integer you want to add: "))
    integers.append(integer)
  even_list = []
  for integer in integers:
    if (integer % 2 == 0): 
      even_list.append(integer)
  return even_list
print(Even_num())
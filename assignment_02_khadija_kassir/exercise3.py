def String(s):
  reversed_str = ""
  for word in s:
    reversed_str = word + reversed_str
  return reversed_str
user = input("write a word:")
print("Reversed string: ", String(user))
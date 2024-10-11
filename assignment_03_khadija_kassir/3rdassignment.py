#1st function 
def digits(num):
    if (num == 0):
        return 1
    return 1+digits(num/10)
#2nd function : find the max

def max():
    numbers=[]
    elements = int(input("give me  number of elements you will add to the list: "))
    for i in range (elements):
        number=int(input("type the number: "))
        list.append(numbers)
    def maxRecursively(s):
        if len(s) ==1:
            return s[0]
        else: 
            return max(s[0], maxRecursively(s[1:]))
        return maxRecursively (numbers)

#3rd function: 

def tags (html, tag): 
    if "<"+ tag + ">" in html or "</" + tag + ">" in html:
         if "<" + tag + ">" in html:
            html = html.replace("<" + tag + ">", "", 1)
         if "</" + tag + '>' in html:
            html = html.replace("</" + tag + ">", "", 1)
         return 1 + tags (html, tag)
    else:
        return 0
    
 #main function: 
def main():
  
 htmlPart ="""
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>
"""  
 while True:
    print("1 to  count digits") 
    print("2 to  find max")
    print("3 to count tags") 
    print("4 to break")
    choice = int(input("give me your choice: "))

    if choice == 1:
      number = int(input("give me an integer: "))
      print(digits(number))
    elif choice == 2:
      print(max())
    elif choice == 3:
      tag_name = input("give me the tag name: ")
      print("Number of the tags:", tags(htmlPart, tag_name))
    elif choice == 4:
      break
    else:
      print("error, please try again another choice")
   
if __name__ == "__main__":
  main()


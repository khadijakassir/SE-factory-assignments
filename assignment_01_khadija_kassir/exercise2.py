n = int (input("give me a positive integer : "))
multiplication = 1
#start from number 1 as given between 1 and n
a = 1
while a < n: #inclusive
    if a%2 == 1: # number is odd
        multiplication *=a 
        if multiplication > 100:
            print("multiplication exceeded")
            break
        elif multiplication < 100: 
            print ("final value = ", multiplication) 
             
    a += 1 #to go to next number 

else:
     print(1)    

     









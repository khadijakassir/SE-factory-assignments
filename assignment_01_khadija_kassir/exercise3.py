scores = []
score = 0
print(" to stop giving scores give me -1")
while (score > -1 ) :
    score = int(input("give me your scores:  "))
    scores.append(score)
    if score == -1:
        average = sum(scores)/ len(scores)
        print(" your score is: ", average)
            


 
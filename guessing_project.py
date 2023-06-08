import random
#thonniya pole no. print cheithu varan randrang UPAYOGIKKUNNATH. ivide x nte ullil 0 to 5 vareyulla oru no. store cheithirikkunnu
# x=random.randrange(0,5)
# print(x)
flowers=["rose","jasmine","lilly","lotus"]
print("List=",flowers)
selection=str(input("Enter your selection"))
computer_guess=random.randrange(0,3)
guess=flowers[computer_guess]
if selection==guess:
    print("you won")
     
else:
    print("you failed")
print("computer selection=",guess)
print("your selection=",selection)







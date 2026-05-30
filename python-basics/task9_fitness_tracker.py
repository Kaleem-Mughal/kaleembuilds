print("Personal Fitness & Reading Tracker")
name=input("Enter your name :").capitalizeO()
age=int(input("Enter your age :"))
book=[]
b1=input("Enter the 1st Book you have read :")
b2=input("Enter the 2nd Book you have read :")
b3=input("Enter the 3rd Book you have read :")
book.append(b1)
book.append(b2)
book.append(b3)
pushups=[]
push1=int(input("Enter  the push ups of 1st day :"))
push2=int(input("Enter  the push ups of 2nd day :"))
push3=int(input("Enter  the push ups of 3rd day :"))
push4=int(input("Enter  the push ups of 4th day :"))
push5=int(input("Enter  the push ups of 5th day :"))
pushups.append(push1)
pushups.append(push2)
pushups.append(push3)
pushups.append(push4)
pushups.append(push5)
genre=input("Your favorite Genre :").capitalize()
print("Name is Capitalized",name.capitalize())
book_tuple=tuple(book)
print("Max pushups :",max(pushups))
print("Min pushups :",min(pushups))
avg_pushups=(push1+push2+push3+push4+push5)/5
print("Avg pushups :",avg_pushups)
total_pushups=push1+push2+push3+push4+push5
print("Total pushups :",total_pushups)
print("Full Tracker summary is below")
print("Your Name :",name)
print("Your age :",age)
print("Your Genre :",genre)
print(" Your Books :",book_tuple)
print("Total books :",len(book))
print("All pushups :",total_pushups)
print("Highest push ups :",max(pushups))
print("Lowest push ups :",min(pushups))
print("Avg push ups :",avg_pushups)
print("Total push ups :",total_pushups)
print("Avg pushups above 30? :",avg_pushups>30)
print("Does name ends with vowel? :",name.endswith("a") or name.endswith("e") or name.endswith("i") or name.endswith("o") or name.endswith("u"))
if avg_pushups>50:
    if age<25:
        print("Elite Athlete")
    else :
        print("Advance Athlete")
elif avg_pushups>30:
    if age<25:
        print("Intermediate")
    else:
        print("Active")
else:
    print("Just getting started")
if genre=="Fiction":
    print("Try : Atomic Habit")
elif genre=="Self help":
    print("Try : The Alchemist")
elif genre=="Technical":
    print("Try : Clean Code")
else:
    print("Explore more genre")

a=input("Enter your name :")
b=input("YOur subject : ")
c=int(input("Enter your marks :"))
a=a.capitalize()
print("Your name :",a)
print("Sub ends with 's' ? ",b.endswith("s"))
print("Sub replaced as :",b.replace("mathematics","Math"))
print("Position of a in name (index):",a.find("a"))
print("Quantity of a in name :",a.count("a"))
if c>=90 and c<=100:
    print("Grade A")
    if c==100:
        print("Perfect score")
    else:
        print("Excellent!")
elif c>=80:
    print("Grade B")
elif c>=70:
    print("Grade C")
elif c>=60:
    print("Grade D")
elif c>=0:
    print("Fail")
else:
    print("Enter valid marks")

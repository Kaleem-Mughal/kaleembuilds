name=input("Enter full name :")
age=int(input("Enter your age :"))
marks=[]
s1=int(input("Enter marks of subject 1 :"))
s2=int(input("Enter marks of subject 2 :"))
s3=int(input("Enter marks of subject 3 :"))
s4=int(input("Enter marks of subject 4:"))
marks.append(s1)
marks.append(s2)
marks.append(s3)
marks.append(s4)
dep=input("Enter your Department :").upper()
city=input("City of residence :").capitalize()
print("Total marks :",s1+s2+s3+s4)
percentage=(s1+s2+s3+s4)/400 *100
print("Their percentage :", percentage)
print("Highest marks :",max(marks))
print("Lowest marks",min(marks))
tup=tuple(marks)
print("Capitalized name :",name.upper())
print("Capitilized city :",city.upper())
print("Full Admission form is as follows")
print("Name :",name)
print("Age :",age)
print("City :",city)
print("Obtained marks :",s1+s2+s3+s4)
print("Total marks : 400")
print("Percentage :",percentage)
print("Highest marks :",max(marks))
print("Lowest marks",min(marks))
print("Percentage above 80 :",percentage>80)
same=name[0]==city[0]
print("Name and city starts with same letter :",same)
if percentage>=80:
    if dep=="CS":
        print("Admitted to CS")
    elif dep=="MEDICAL":
        print("Admitted to Medical")
    elif dep=="BUSINESS":
        print("Admitted to Business")
    else:
        print("We are sorry")
elif percentage >=60 and percentage<80:
    if dep=="CS":
        print("Admitted to CS evening")
    elif dep=="MEDICAL":
        print("Not eligible for Medical")
    elif dep=="BUSINESS":
        print("Admitted to Business evening")
    else:
        print("We are sorry")
elif percentage<60:
    print("Admission rejected for all department")
else:
    print("Enter percentage from 0-100")
print("Scholarship Information")
if percentage>=90 and age<=20:
    print("Full Scholarship")
elif percentage>=80 and age<=25:
    print("50% Scholarship")
elif percentage>=70:
    print("25% Scholarship")
elif percentage<70:
    print("No Scholarship")
else:
    print("Enter correct marks/percentage")

p=[]
name=input("Enter your name :").capitalize()
age=int(input("Enter your age :"))
symp1=input("Symptom 1st :").lower()
symp2=input("Symptom 2nd :").lower()
symp3=input("Symptom 3rd :").lower()
p.append(symp1)
p.append(symp2)
p.append(symp3)
blood=input("Enter your blood type :").upper()
temp=float(input("Enter your temprature in Fahrenheit :"))
temp_cel=(temp-32)*5/9
print("Temprature in Celsius :",temp_cel)
print("Name :",name.capitalize())
tup=tuple(p)
print("Patient summary")
print("P.name :",name)
print("P.age :",age)
print("P.symp :",p)
print("Patient name ends with vowel ? :",name.endswith("a") or name.endswith("e") or name.endswith("i") or name.endswith("o") or name.endswith("u"))
print("Temprature is fever :",temp_cel>37.5)
if age<12 or age>60:
    print("High risk")
elif temp_cel>39:
    print("Critical")
elif blood=="O" and age>40:
    print("Monitor closely")
else:
    print("Stable")
print("Does patient have headache?","headache" in tup)
print("Length of sumps :",len(tup))

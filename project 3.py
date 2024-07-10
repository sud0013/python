# underweight:BMI less than 18.5
# Normal weight:BMI between 18.5 and 24.9
# Overweight:BMI between 25 and 29.9
# Obesity:
# Class I (Moderate obesity): BMI between 30 and 34.9
# Class II (Severe obesity): BMI between 35 and 39.9
# Class III (Very severe or morbid obesity): BMI of 40 and above
name=input("enter your name:")
weight=int(input("enter your weight in kg:"))
height=float(input("enter your height in metre:"))
BMI=weight/(height**2)
print(BMI)
if BMI<18.5:
    print("underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("normal weight")
elif BMI>=25 and BMI<=29.9:
    print("over weight")
elif BMI>30:
    if BMI>=30 and BMI<=34.9:
        print("moderate obesity")
    elif BMI>=35 and BMI<=39.9:
        print("severe obesity")
    else:
        print("very severe or morbid obesity")
else:
    print("enter correct values")
print("BMI value of",name,"is",BMI)
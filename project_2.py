#Use conditional statement and get the marks
# print the result for the following marks
# 90 to 100=A grade
# 80 to 90=B grade
# 70 to 80= C grade
# 60 to 70= D grade
# below 60= E grade
# Get the student name and marks, print the total of marks,average and  give grades according to marks

name=input("enter your name:")
print(name)

maths=float(input("enter maths marks:"))
science=float(input("enter science marks:"))
social=float(input("enter social marks:"))
english=float(input("enter english marks:"))
tamil=float(input("enter tamil marks:"))
IT=float(input("enter IT marks:"))

# total marks

total_marks=maths+science+social+english+tamil+IT
print(total_marks)
# average mark
avg_marks=(maths+science+social+english+tamil+IT)/6
print(avg_marks)

if avg_marks>=90 and IT<=100 :
    print("a grade")
elif avg_marks>=80 and IT<90 :
    print("b grade")
elif avg_marks>=70 and avg_marks<80 :
    print("c grade")
elif avg_marks>=60 and avg_marks<70 :
    print("d grade")
elif avg_marks<60:
    print("e grade")
else:
    print("enter your mark correctly")
mark = []
print("Enter 5 different marks : ")
x=1
for i in range(5):
    mark.append(int(input("sub " + str(x) + " marks =")))
    x=x+1

p = (sum(mark)/500)*100
print("percentage of students = ",p)

if p>=90:
    print("Grade A")
elif p>=80:
    print("Grade B")
elif p>=70:
    print("Grade C")
elif p>=60:
    print("Grade D")
elif p>=40:
    print("Grade E")
else:
    print("Grade F")
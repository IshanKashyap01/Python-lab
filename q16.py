marks = []
print("Enter marks of 3 subjects: ")
for i in range(3):
	marks.append(int(input()))
percent = ( sum(marks) / 300 ) * 100

if(percent >= 40 and min(marks) >= 33):
	print("Pass")
else:
	print("Fail")

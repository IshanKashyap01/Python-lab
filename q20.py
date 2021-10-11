scheme = {"Excellent": [90, 100], "A": [80, 89], "B": [70, 79], "C": [60, 69], "D": [50, 59], "Fail": [0, 49]}

marks = int(input("Enter your marks: "))

for i in scheme:
	if marks in range(int(scheme[i][0]), int(scheme[i][1])):
		print("Your grade is", i)
		break

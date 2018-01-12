
grade= int(input("Enter Marks: "))

letterGrade = "F"
if grade >= 90 :
	letterGrade = "A"
if grade >= 80 :
	letterGrade = "B"
if grade >= 70 :
	letterGrade = "C"
if grade >= 60 :
	letterGrade = "D"

print(letterGrade)

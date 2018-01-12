
password = "changeme"

noOfattempts=0

while input("Enter password: ") != password and noOfattempts < 5:
    print("Try Again")
    noOfattempts+=1;

if noOfattempts == 5:
    print("Access denied,please enter to exit and contact security to reset your password")

if password=="changeme" and noOfattempts <5:
    print("Password Accepted")
print("No of attempts :",noOfattempts+1)

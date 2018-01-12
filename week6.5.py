
password = "changeme"

noOfattempts=0

while input("Enter password: ") != password:
    print("Try Again")
    noOfattempts+=1;
    
if password == "changeme":
   print("Password Accepted")
print("No of attempts :",noOfattempts+1)



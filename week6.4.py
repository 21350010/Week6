
richterScale=float(input("Enter magnitude : "))

if richterScale >= 8.0:
    print("Most structures fall")
elif richterScale >= 7.0:
    print("Many buildings destroyed")
elif richterScale >=6.0:
    print("Many buildings considerably damaged,some collapse")
elif richterScale >=4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")

age = int(input("your age: "))
gndr = input("what's your gender? (m/f): ")
if gndr == "m":
    if age < 65:
        print("years remaining to the user until retirement", 65 - age)
    else:
        print("you are retired")
elif gndr == "f":
    if age < 60:
        print("years remaining to the user until retirement", 60 - age)
    else:
        print("you are retired")
else:
    print("not correctly selected gender")
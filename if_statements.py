user_age = int(input("What is your age? "))
if user_age > 30:
    print("You are over 30 years old.")
    print("Sorry, you do not qualify")
elif user_age == 30:
    print("You are exaclty 30 years old")
    print("you will need to meet additional conditions to qualify")
else:
    print("You are 30 years old or younger")
    print("Congratulations, you qualify!")

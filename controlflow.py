# basic if else statements
age = 10
if age >=18:
    print("You're eligible to vote")
    print("You're an adult")
else:
    print("You're not eligible to vote")
    print("You're not an adult")

# if - elif - else statements
score = 40
if score >= 90:
    print("A : Excellent")
elif score >=80:
    print(" B : Good Job!")
elif score >=70:
    print(" C : Keep it up!")    

else:
    print("F - NEEDS IMPROVEMENT")




age = 25
has_license = True
weekend= True
holiday= False
raining= True
if age>=18 and has_license:
    print("You can drive")

if weekend or holiday:
    print('no work today')

if not raining:
    print("Lets go outside")
else:
    print("Its raining, Let's stay indoors")




#nested if statements
has_ticket = False
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")



    
bill = float(input("Enter total bill: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
each_person = total / people

print("Tip:", tip)
print("Total bill:", total)
print("Each person pays:", each_person)


# 2nd program

password = input("Enter password: ")

if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password)):
    print("Strong Password")
elif len(password) >= 6:
    print("Moderate Password")
else:
    print("Weak Password")

    # 3rd program
    
    secret = 42
attempts = 0

while attempts < 5:
    guess = int(input("Guess a number (1-100): "))

    if guess < 1 or guess > 100:
        print("Invalid number! Try again.")
        continue

    attempts += 1

    if guess == secret:
        print("Correct! You win.")
        break
    else:
        print("Wrong guess!")

else:
    print("Game Over! You lost.")
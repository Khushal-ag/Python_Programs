n = 25
guess = 8
while guess > 0:
    guess -= 1
    num = int(input("Enter your guess no. = "))
    if num == n:
        print("Congrats!! You guess right\nYou took", 8 - guess, "guesses")
        break
    else:
        if num > n:
            print("Guess a Smaller one")
        else:
            print("Guess a Greater one")
        print("Remaining Guesses ->", guess, end="\n\n")
if guess == 0:
    print("Sorry You are out of guesses")


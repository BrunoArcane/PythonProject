# guess.py
import random

LOW, HIGH = 1, 100
secret = random.randint(LOW, HIGH)
tries = 0

print(f"🎯 I picked a number between {LOW} and {HIGH}. Try to guess it!")

while True:
    guess_txt = input("Your guess: ")
    if not guess_txt.strip().isdigit():
        print("Type a whole number only.")
        continue

    guess = int(guess_txt)
    tries += 1

    if guess < LOW or guess > HIGH:
        print(f"Stay in range {LOW}-{HIGH}.")
        continue

    if guess < secret:
        print("Too low ⬇️")
    elif guess > secret:
        print("Too high ⬆️")
    else:
        print(f"✅ Correct! You got it in {tries} tries.")
        break

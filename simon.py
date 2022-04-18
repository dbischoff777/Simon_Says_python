import random
import os
import time

colors = ["R", "B", "Y", "G"]
simon = ""

for score in range (0, 10):
    simon += random.choice(colors)
    for color in simon:
        if color == "R": print("\033[0;31;40mR\033[0m")
        if color == "B": print("\033[0;34;40mB\033[0m")
        if color == "Y": print("\033[1;33;40mY\033[0m")
        if color == "G": print("\033[0;32;40mG\033[0m")
        time.sleep(1.5)
        os.system("cls")
    guess = input("Repeat: ").upper()
    os.system("cls")
    if guess != simon:
        break


print(f"Game over! Your final score is {score}")

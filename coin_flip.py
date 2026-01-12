# Odd Even Program
import random
import time

print("Welcome to coin flip, press enter to play") # The start page text
input() # What prompts/forces the user to pressx enter to continue
sides = ['Tails', 'Heads'] # Define the sides of the coin
# Loads 101 numbers (0-100) and the time.sleep is waiting time inbetween
for i in range(101):
    print(f"\rLoading... {i}%", end="", flush=True)
    time.sleep(0.05)

print()  # move to next line
result = random.choice(sides)
if result == "Heads":
    print(f"\033[32mResult is {result}\033[0m")  # green
else:
    print(f"\033[31mResult is {result}\033[0m")  # red

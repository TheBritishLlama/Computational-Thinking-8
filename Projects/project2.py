answer = 0
points = 0
misses = 0
deduction = 0
print("")
print("Welcome! Do you want to take a quiz?")
print("")
input (">>> Press ENTER to start ")
print("")
print("How many centimeters are in a meter?")
print("")
print("A: 10, B: 50, C: 100")
print("")
answer = input (">>> ")
if answer == "C":
    points += 1
elif answer == "A" or answer == "B":
    misses -= 2
print("")
answer = 0
print("What is 19x9?")
print("")
print("A: 171, B: 200, C: 162")
print("")
answer = input(">>> ")
if answer == "A":
    points += 1
elif answer == "C" or answer == "B":
    misses -= 2
print("")
answer = 0
print("What is the capital of Norway?")
print("")
print("A: Oslo, B: Stockholm, C: Canberra")
print("")
answer == input(">>> ")
if answer == "A":
    points += 1
elif answer == "C" or answer == "B":
    misses -= 1
print("")
answer = 0
print("What is the lightest element?")
print("")
print("A: Oxygen, B: Hydrogen, C: Osmium")
print("")
answer = input(">>> ")
if answer == "B":
    points += 2
elif answer == "A" or answer == "C":
    misses -= 2
print("")
answer = 0
print("What is the chemical symbol of gold?")
print("")
print("A: An, B: Gd, C: Au")
print("")
answer = input(">>> ")
if answer == "C":
    points += 2
elif answer == "A" or answer == "B":
    misses -= 1
print("")
print("Calculating your score now...")
print("")
if misses == 0 and points == 6:
    print("Incredible, you aced the test!")
if misses <= -0.1:
    print(f"Your score was {6 + misses} out of 6.")
print("")
print("Thanks for playing!")
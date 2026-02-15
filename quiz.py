# Score
score = 0

# Questions
que1 = "What color is GRASS?"
que2 = "What is 9 + 4?"
que3 = "What is Artifical Intelligence for short?"

# Final
final = "Was this quiz easy?"
que4 = final

# Answers
ans1 = "Green"
ans2 = "13"
ans3 = "AI"
ans4 = "yes"
print(que1)
answer = str(input("Answer Here: "))
# Question 1
if answer == ans1:
  print(f"Correct answer!")
else:
  print(f"Wrong answer. The correct answer was: {ans1}")
print(que2)
answer = str(input("Answer Here: "))
# Question 2
if answer == ans2:
  print(f"Correct answer!")
else:
  print(f"Wrong answer. The correct answer was: {ans2}")
print(que3)
answer = str(input("Answer Here: "))

# Question 2
if answer == ans3:
  print(f"Correct answer!")
else:
  print(f"Wrong answer. The correct answer was: {ans3}")
print(que4)
answer = str(input("Answer Here: "))

# Question 4
if answer == ans4:
  print(f"Correct answer!")
else:
  print("Wrong answer. The correct answer was: actually there is no answer")
print("Thanks for playing, made with luv by me lol")
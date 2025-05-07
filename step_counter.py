print ("Welcome to the daily step counter register!")
daily_goal = int(input("What is your daily goal? : "))
steps = int(input("How many step have you made so far? : "))

if daily_goal > steps:
    print (f"keep going you have {daily_goal - steps} steps left!")
else:
    print("Congratulations! You completed your daily goal")
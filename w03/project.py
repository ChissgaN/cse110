grade_percentage = int(input("Enter your grade percentage: "))

# Determine the letter grade
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

# Determine the "+" or "-" sign
if letter != "F": 
    last_digit = grade_percentage % 10
    if last_digit >= 7:
        sign = "+"
    elif last_digit < 3:
        sign = "-"
    else:
        sign = ""
    if letter == "A" and sign == "+":
        sign = ""
else:
    sign = ""

print(f"Your grade is: {letter}{sign}")

# Check if the user passed the course
if grade_percentage >= 70:
    print("Congratulations! You passed the course.")
else:
    print("You did not pass the course. Better luck next time!")

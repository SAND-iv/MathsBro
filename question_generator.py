import random

def generate_math_problem(level):
    
    #Generate a math problem based on the specified difficulty level.
    #- Demo: Addition only, numbers between 0 and 5.
    #- Easy: Addition and subtraction, numbers between 0 and 10.
    #- Medium: Same as Easy.
    #- Hard: Addition, subtraction, and multiplication, numbers between 0 and 20.

    settings = {
        "demo": (0, 5, ["+"]),
        "easy": (0, 10, ["+", "-"]),
        "medium": (0, 10, ["+", "-"]),
        "hard": (0, 20, ["+", "-", "*"]),
    }

    # Get the range and operations for the level
    num_range = settings[level][:2]
    operations = settings[level][2]

    # Generate random numbers and operation
    num1 = random.randint(num_range[0], num_range[1])
    num2 = random.randint(num_range[0], num_range[1])
    operator = random.choice(operations)

    # Calculate the correct answer
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2

    return f"{num1} {operator} {num2}", answer

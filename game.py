from question_generator import generate_math_problem
from file_manager import save_game_results

def run_game_round(level, session_id, file_handle):
    
    #Conduct a single round of the game.
    #- Generate and display math questions.
    #- Record user answers and calculate score.
    
    question_counts = {"demo": 3, "easy": 5, "medium": 10, "hard": 10}
    total_questions = question_counts[level]
    correct_count = 0
    all_questions = []

    for _ in range(total_questions):
        # Generate a math question
        question, correct_answer = generate_math_problem(level)

        # Get user input with validation
        while True:
            try:
                user_input = int(input(f"{question} = "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # Check answer and update results
        if user_input == correct_answer:
            correct_count += 1
            all_questions.append((question, user_input, True, None))
        else:
            all_questions.append((question, user_input, False, correct_answer))

    # Calculate percentage score
    score_percentage = (correct_count / total_questions) * 100

    # Save results to the session file
    save_game_results(
        file_handle, session_id, level, all_questions, correct_count, total_questions, score_percentage
    )

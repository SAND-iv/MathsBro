from datetime import datetime
import random

def create_unique_filename():
    
    #Generate a unique filename for the session using date, time, and a random number.

    now = datetime.now()
    date_part = now.strftime("%Y%m%d")
    time_part = now.strftime("%H%M")
    random_part = random.randint(100, 999)
    return f"{date_part}_{time_part}_{random_part}.txt"

def save_game_results(file_handle, session_id, level, questions, correct_count, total_questions, score):
    
    #Save the results of a game session to a file in the specified format.
    #- Includes session date, time, question results, and summary statistics.

    now = datetime.now()
    session_date = now.strftime("%Y-%m-%d")
    session_time = now.strftime("%H:%M:%S")

    # Write session metadata
    file_handle.write(f"Date   : {session_date}\n")
    file_handle.write(f"Time   : {session_time}\n\n")
    file_handle.write(f"Session {session_id}\n")
    file_handle.write("Result sheet\n")

    # Write each question result
    for question, user_answer, is_correct, correct_answer in questions:
        if is_correct:  # If answer is correct
            symbol = "√"
            file_handle.write(f"{symbol} {question} = {user_answer}\n")
        else:  # If answer is incorrect
            symbol = "X"
            file_handle.write(f"{symbol} {question} = {user_answer} correct answer is {correct_answer}\n")

    # Write summary statistics
    file_handle.write(f"\nTotal questions  : {total_questions}\n")
    file_handle.write(f"Correct questions: {correct_count}\n")
    file_handle.write(f"Marks            : {score:.1f}%\n")
    file_handle.write(f"Level            : {level.capitalize()}\n\n")

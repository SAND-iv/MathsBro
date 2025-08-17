import sys
from game import run_game_round
from file_manager import create_unique_filename

def main():
    
    #Main function to start the MathsBro game.
    #Handles game initialization, dynamic difficulty changes, and session management.
    
    # Set initial difficulty based on command-line arguments
    if len(sys.argv) == 1:
        difficulty = "demo"
    else:
        arg_map = {"-e": "easy", "-m": "medium", "-h": "hard"}
        difficulty = arg_map.get(sys.argv[1], "demo")

    # Generate a unique filename for session results
    filename = create_unique_filename()
    session_id = 1  # Initialize session counter

    with open(filename, "w", encoding="utf-8") as result_file:
        print("Welcome to MathsBro Game!")
        print(f"Starting in {difficulty.capitalize()} mode...\n")

        while True:
            # Run a game round
            run_game_round(difficulty, session_id, result_file)
            session_id += 1

            # Ask if the user wants to play another round
            while True:
                play_again = input("Would you like to play another game? (yes/no): ").strip().lower()
                if play_again in ["yes", "y"]:
                    break
                elif play_again in ["no", "n"]:
                    print("Thank you for playing! Your results have been saved.")
                    return  # Exit the main loop and program
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            # Allow the user to select a new difficulty level
            while True:
                difficulty = input(
                    "Select difficulty for the next game (demo, easy, medium, hard): "
                ).strip().lower()
                if difficulty in ["demo", "easy", "medium", "hard"]:
                    break
                else:
                    print("Invalid input. Please enter 'demo', 'easy', 'medium', or 'hard'.")


main()

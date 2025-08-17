MathsBro
MathsBro is a Python-based console game designed to help users practice and improve their arithmetic skills through interactive math problems. The game generates random questions based on user-selected difficulty levels (Demo, Easy, Medium, Hard), provides real-time feedback, and saves session results to uniquely named text files for progress tracking. Built with modular design principles, MathsBro demonstrates key programming concepts such as input validation, file handling, and dynamic user interaction.
Features

Dynamic Question Generation: Creates random math problems (addition, subtraction, multiplication) with varying complexity based on the chosen difficulty level:

Demo: Addition with numbers 0–5 (3 questions).
Easy: Addition and subtraction with numbers 0–10 (5 questions).
Medium: Addition and subtraction with numbers 0–10 (10 questions).
Hard: Addition, subtraction, and multiplication with numbers 0–20 (10 questions).


Real-Time Feedback: Displays "√" for correct answers and "X" with the correct answer for incorrect ones.
Session Tracking: Saves session details (date, time, questions, answers, and scores) to a unique text file.
User-Friendly Interface: Menu-driven flow allows users to select difficulty levels, play multiple rounds, or exit gracefully.
Robust Design: Includes input validation and error handling for a seamless experience.

Installation
To set up and run MathsBro on your local machine, follow these steps:

Clone the Repository:
bashgit clone https://github.com/your-username/MathsBro.git

Navigate to the Project Directory:
bashcd MathsBro

Ensure Python is Installed:

MathsBro requires Python 3.x. Verify installation with:
bashpython --version

If Python is not installed, download it from python.org.



Usage

Run the Game:
bashpython mathbro.py

Select a Difficulty Level:

Choose from Demo, Easy, Medium, or Hard when prompted.


Answer Questions:

Enter integer answers for the displayed math problems.
Receive immediate feedback on correctness.


Review Results:

After completing a session, view your score and performance summary on the console.
Check the generated text file (e.g., 20250817_1321_123.txt) in the project directory for detailed session results.


Play Again or Exit:

Choose to start a new session with a different difficulty or exit the game.



Project Structure

mathbro.py: Main script to initialize and run the game.
game.py: Manages game rounds, user input, and scoring.
question_generator.py: Generates random math problems based on difficulty.
file_manager.py: Handles creation and storage of session result files.

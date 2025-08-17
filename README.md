# MathsBro 🎮🧮

**MathsBro** is an engaging Python-based console game designed to help users sharpen their arithmetic skills in a fun and interactive way. The game generates random math problems tailored to your chosen difficulty level, provides real-time feedback, and tracks your progress through uniquely saved session files. Built with modular design, MathsBro showcases key programming concepts including input validation, file handling, and dynamic user interaction.

### 🌟 Features

* **Dynamic Question Generation:**
  Tailors math problems based on difficulty:

  * **Demo:** Addition (0–5), 3 questions
  * **Easy:** Addition & Subtraction (0–10), 5 questions
  * **Medium:** Addition & Subtraction (0–10), 10 questions
  * **Hard:** Addition, Subtraction & Multiplication (0–20), 10 questions

* **Real-Time Feedback:**
  Instant correctness notifications: "√" for correct answers, "X" with the correct answer for mistakes.

* **Session Tracking:**
  Every game session is saved with date, time, questions, answers, and score in a uniquely named text file for easy progress tracking.

* **User-Friendly Interface:**
  Menu-driven navigation allows selection of difficulty, multiple rounds, or graceful exit.

* **Robust Design:**
  Input validation and error handling ensure a smooth, seamless experience.

### ⚡ Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/MathsBro.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd MathsBro
   ```

3. **Ensure Python 3.x is Installed:**

   ```bash
   python --version
   ```

   If Python is not installed, download it from [python.org](https://www.python.org/).

### ▶️ Usage

1. **Run the Game:**

   ```bash
   python mathbro.py
   ```

2. **Select a Difficulty Level:**
   Choose from Demo, Easy, Medium, or Hard.

3. **Answer Questions:**
   Input integer answers and get instant feedback.

4. **Review Results:**
   See your score on the console and check the generated session file (e.g., `20250817_1321_123.txt`) for details.

5. **Play Again or Exit:**
   Start a new session or exit the game gracefully.

### 📁 Project Structure

* `mathbro.py` – Main script to launch the game
* `game.py` – Manages game rounds, input, and scoring
* `question_generator.py` – Generates math problems based on difficulty
* `file_manager.py` – Handles session file creation and storage

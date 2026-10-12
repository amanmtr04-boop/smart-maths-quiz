
import random

questions = [
    {
        "question": "What is 15 x 8?",
        "options": ["100", "120", "130", "140"],
        "answer": "120",
        "explanation": "15 x 8 = 120."
    },
    {
        "question": "What is the square of 13?",
        "options": ["156", "169", "179", "196"],
        "answer": "169",
        "explanation": "13 x 13 = 169."
    },
    {
        "question": "What is 3/4 of 100?",
        "options": ["25", "50", "75", "80"],
        "answer": "75",
        "explanation": "100 x 3/4 = 75."
    },
    {
        "question": "What is the cube of 4?",
        "options": ["16", "32", "64", "48"],
        "answer": "64",
        "explanation": "4 x 4 x 4 = 64."
    },
    {
        "question": "Solve: 5x = 45. What is x?",
        "options": ["5", "8", "9", "10"],
        "answer": "9",
        "explanation": "Divide both sides by 5: x = 9."
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "14"],
        "answer": "12",
        "explanation": "12 x 12 = 144."
    },
    {
        "question": "What is 25% of 200?",
        "options": ["25", "40", "50", "75"],
        "answer": "50",
        "explanation": "25% means one-fourth. 200 / 4 = 50."
    },
    {
        "question": "What is 2 to the power of 5?",
        "options": ["10", "16", "25", "32"],
        "answer": "32",
        "explanation": "2 x 2 x 2 x 2 x 2 = 32."
    },
    {
        "question": "How many degrees are in a right angle?",
        "options": ["45", "90", "180", "360"],
        "answer": "90",
        "explanation": "A right angle measures 90 degrees."
    },
    {
        "question": "What is the perimeter of a square with side 6 cm?",
        "options": ["12 cm", "18 cm", "24 cm", "36 cm"],
        "answer": "24 cm",
        "explanation": "Perimeter = 4 x side = 4 x 6 = 24 cm."
    }
]


def play_quiz():
    print("\n" + "=" * 40)
    print("       SMART MATHS QUIZ")
    print("=" * 40)

    name = input("Enter your name: ").strip()

    if not name:
        name = "Player"

    score = 0
    random_questions = questions.copy()
    random.shuffle(random_questions)

    for number, question in enumerate(random_questions, start=1):
        print(f"\nQuestion {number}/{len(random_questions)}")
        print(question["question"])

        options = question["options"].copy()
        random.shuffle(options)

        for letter, option in zip("ABCD", options):
            print(f"{letter}. {option}")

        while True:
            choice = input("Your answer (A/B/C/D): ").strip().upper()
            if choice in ["A", "B", "C", "D"]:
                break
            print("Please enter A, B, C, or D.")

        selected_answer = options["ABCD".index(choice)]

        if selected_answer == question["answer"]:
            print("Correct! Well done!")
            score += 1
        else:
            print("Not quite!")

        print("Explanation:", question["explanation"])

    percentage = score / len(random_questions) * 100

    print("\n" + "=" * 40)
    print("           QUIZ RESULTS")
    print("=" * 40)
    print("Player:", name)
    print("Score:", score, "/", len(random_questions))
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Outstanding! Perfect score!")
    elif percentage >= 70:
        print("Great work! Keep practising.")
    elif percentage >= 40:
        print("Good effort! You are improving.")
    else:
        print("Keep learning. You can do it!")

    print("=" * 40)


while True:
    play_quiz()
    again = input("\nWould you like to play again? (yes/no): ").strip().lower()

    if again not in ["yes", "y"]:
        print("Thanks for playing Smart Maths Quiz!")
        break

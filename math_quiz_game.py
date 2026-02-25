import random 

print("  Welcome to the Quiz Game  ")

def generate_question():
    number1 = random.randint(1,100)
    number2 = random.randint(1,50)
    operations = random.choice(["+", "/", "*", "-"])

    if operations == "+":
        correct_answer = number1 + number2
    elif operations == "-":
        correct_answer = number1 - number2
    elif operations == "*":
        correct_answer = number1 * number2
    else:
        correct_answer = round(number1 / number2)

    question_text = f"What is {number1} {operations} {number2}?"
    return question_text, correct_answer


def play_questions():
    score = 0
    total_questions = 8

    for _ in range(total_questions):
        question, answer = generate_question()
        print("\n", question)
        user_input = int(input("Your answer: "))

        if user_input == answer:
            print("Congratulations, correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}")

    print(f"Final score: {score} / {total_questions}")


while True:
    play_questions()
    play_again = input("Do you want to play again? Yes or No: ").lower()
    if play_again != "yes":
        print("Thanks for playing")
        break
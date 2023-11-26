import random

# Importing question sets from the questions module
from questions import html_questions, c_questions, java_questions, python_questions, current_affairs_questions

def display_question(question_number, question_data):
    # Function to display a single question
    if isinstance(question_data, dict):
        print(f"\nQuestion {question_number}: {question_data['question']}")
        for option, text in question_data["options"].items():
            print(f"  {option}. {text}")
        user_answer = input("Your choice (A/B/C/D): ")
        return user_answer
    elif isinstance(question_data, list):
        # If it's a list of questions, return an empty string
        return ""

def get_questions(main_category, sub_category):
    # Function to get the selected set of questions based on main and sub-categories
    all_questions = {
        "Programming Languages": {
            "HTML": html_questions,
            "C": c_questions,
            "Java": java_questions,
            "Python": python_questions,
        },
        "Current Affairs": current_affairs_questions,
    }

    if main_category == "Current Affairs" and sub_category is None:
        # If the main category is Current Affairs, return all questions in that category
        return all_questions.get(main_category, [])
    elif main_category in all_questions and sub_category in all_questions[main_category]:
        # If both main and sub-categories are valid, return the corresponding set of questions
        return all_questions[main_category][sub_category]
    else:
        # If the categories are invalid or not found, return an empty list
        return []

def select_main_category():
    # Function to select the main category
    print("\nChoose a main category:")
    print("1. Programming Languages")
    print("2. Current Affairs")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        return "Programming Languages"
    elif choice == "2":
        return "Current Affairs"
    else:
        # If an invalid choice is entered, prompt the user to try again
        print("Invalid choice. Please try again.")
        return select_main_category()

def select_sub_category(main_category):
    # Function to select the sub-category for Programming Languages
    if main_category == "Programming Languages":
        print("\nChoose a subcategory for Programming Languages:")
        print("1. HTML")
        print("2. C")
        print("3. Java")
        print("4. Python")
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            return "HTML"
        elif choice == "2":
            return "C"
        elif choice == "3":
            return "Java"
        elif choice == "4":
            return "Python"
        else:
            # If an invalid choice is entered, prompt the user to try again
            print("Invalid choice. Please try again.")
            return select_sub_category(main_category)
    elif main_category == "Current Affairs":
        pass

def display_result(score):
    # Function to display the final quiz result
    print(f"\nYour final score is: {score}")
    if score >= 5:
        print("Congratulations! You did well.")
    else:
        print("Better luck next time. Keep practicing!")

def play_quiz(main_category, sub_category):
    # Function to play the quiz
    selected_questions = get_questions(main_category, sub_category)
    
    max_questions = min(5, len(selected_questions))  # Set the maximum number of questions
    random.shuffle(selected_questions)  # Shuffle the questions randomly

    correct_answers = 0

    for i, question_data in enumerate(selected_questions[:max_questions], start=1):
        # Display each question and get the user's answer   
        print(f"\nQuestion {i}: {question_data['question']}")
        for option, text in question_data['options'].items():
            print(f"  {option}. {text}")

        user_answer = input("Your choice (A/B/C/D): ").upper()

        if user_answer == question_data["correct_answer"].upper():
            # If the user's answer is correct, increment the correct answers count
            print("Correct! You earned +2 points.\n")
            correct_answers += 1
        elif user_answer:
            # If the user's answer is wrong, prompt to try again
            print("Wrong! Try again.\n")
        
    # Calculate the final score based on the total number of correct answers
    score = correct_answers * 2
    return score

def play_again():
    # Function to check if the player wants to play again
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    return choice == "yes"

def main():
    # Main function to run the quiz
    print("********************************************")
    print("**  Welcome to the Celebral Champions!    **")
    print("********************************************")
    
    player_name = input("\nEnter your name: ").capitalize()
    
    print(f"\nHello, {player_name}! Welcome to the Celebral Champions.")
    print("\nTest your knowledge across Various Programming Languages and Current Affairs.\n")
    print("Answer questions to earn points and see how well you can score.")
    print("Let's get started!\n")

    while True:
        main_category = select_main_category()
        sub_category = select_sub_category(main_category)

        score = play_quiz(main_category, sub_category)
        display_result(score)

        if not play_again():
            print(f"\nThanks for playing the Celebral Champions {player_name}. Goodbye!")
            break

# Run the main function to start the quiz
main()

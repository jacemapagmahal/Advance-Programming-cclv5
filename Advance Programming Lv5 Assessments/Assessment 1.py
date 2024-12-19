import random

# Function to display the difficulty menu
def displayMenu():
    print("Welcome to Maths Quiz")
    print("Please choose a difficulty level:")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    choice = input("Enter 1, 2, or 3: ")
    return choice

# Function to generate a random integer within a given range based on difficulty level
def randomInt(difficulty):
    if difficulty == '1':  # Easy: single digit numbers
        return random.randint(1, 9)
    elif difficulty == '2':  # Moderate: double digit numbers
        return random.randint(10, 99)
    elif difficulty == '3':  # Advanced: 4-digit numbers
        return random.randint(1000, 9999)

# Function to decide whether the problem is addition or subtraction
def decideOperation():
    return random.choice(['+', '-'])

# Function to display a problem and accept the user's answer
def displayProblem(num1, num2, operation):
    print(f"What is {num1} {operation} {num2}?")
    answer = input("Your answer: ")
    return answer

# Function to check if the user's answer is correct
def isCorrect(user_answer, correct_answer):
    return user_answer == correct_answer

# Function to display the results and rank the user
def displayResults(score):
    print(f"Your final score is {score} out of 100.")
    if score >= 90:
        print("Grade: A+")
    elif score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    else:
        print("Grade: F")

# Main function to run the quiz
def startQuiz():
    while True:
        # Display the difficulty menu and get user's choice
        difficulty = displayMenu()
        
        # Initialize variables for the game
        score = 0
        
        # Start the quiz: 10 questions
        for i in range(10):
            # Generate random numbers based on difficulty level
            num1 = randomInt(difficulty)
            num2 = randomInt(difficulty)
            operation = decideOperation()
            
            # Display the problem and get the user's answer
            user_answer = displayProblem(num1, num2, operation)
            
            # Calculate the correct answer
            if operation == '+':
                correct_answer = num1 + num2
            else:
                correct_answer = num1 - num2
                
            # Check if the answer is correct
            if isCorrect(int(user_answer), correct_answer):
                score += 10
                print("Correct! You earned 10 points.")
            else:
                # If the first answer is wrong, give them one more chance
                print("Incorrect. Try again.")
                user_answer = input("Your answer: ")
                if isCorrect(int(user_answer), correct_answer):
                    score += 5
                    print("Correct on second try! You earned 5 points.")
                else:
                    print(f"Incorrect again. The correct answer was {correct_answer}.")
        
        # Display the final results and ranking
        displayResults(score)
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

# Start the quiz game
if __name__ == "__main__":
    startQuiz()
1
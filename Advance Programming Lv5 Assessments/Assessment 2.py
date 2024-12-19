import random

# Function to load jokes from the file
def load_jokes(filename):
    try:
        with open(filename, 'r') as file:
            # Read lines, strip extra spaces, and make sure they're not empty
            jokes = [line.strip() for line in file.readlines() if line.strip()]
            # Debugging: Print the jokes to see if the list is populated
            print(f"Loaded jokes: {jokes}")  
        return jokes
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to display a random joke
def tell_joke(jokes):
    if not jokes:  # If there are no jokes, print an error message
        print("No jokes available to tell.")
        return
    joke = random.choice(jokes)
    setup, punchline = joke.split("?", 1)  # Split setup and punchline
    print(f"Setup: {setup}?")  # Show the setup
    input("Press Enter to see the punchline...")  # Wait for the user to press Enter
    print(f"Punchline: {punchline.strip()}")  # Show the punchline

# Main function to run the joke program
def main():
    # Use a raw string for the file path (option 1)
    jokes = load_jokes(r"C‪:\\Users\\Jaceb\Documents\randomJokes.txt")  # Raw string path
    while True:
        user_input = input('Alexa, tell me a Joke (or type "quit" to exit): ').lower()
        if user_input == 'quit':
            print("Goodbye!")
            break
        elif "joke" in user_input:
            tell_joke(jokes)
        else:
            print("I can only tell jokes when you say 'Alexa, tell me a Joke'.")

# Run the program
if __name__ == "__main__":  # Corrected this line
    main()

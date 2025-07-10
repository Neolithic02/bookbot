from stats import get_book_wordcount  # Import the function to count words from stats module
from stats import get_book_lettercount  # Import the function to count letters from stats module
from stats import letter_count  # Import the letter count function from stats module
from stats import sort_letter_count  # Import the function to sort letter counts from stats module
import sys  # Import the sys module for system-specific parameters and functions

# Import necessary functions from stats module



def get_book_text(filepath): # Function to read the book text from a file
    with open(filepath) as f: # Open the file in read mode
        text = f.read() # Read the entire content of the file
    return text # Return the text read from the file


def main():
    if len(sys.argv) == 2:  # Check if command line arguments are provided
        filepath = sys.argv[1]   # Path to the book file
        word_count = get_book_wordcount(filepath)  # Count the words in the book text
        print(f'Found {word_count} total words')  # Display the word count
        lettercountoutput=get_book_lettercount(filepath)  # Count the letters in the book text and display the count
        sorted_letter_count = sort_letter_count(lettercountoutput)  # Sort the letter counts
        for letter, count in sorted_letter_count:
            if letter.isalpha():  # Check if the character is a letter
                print(f'{letter}: {count}') # Print the letter and its count
    else:
        print('Usage: python3 main.py <path_to_book>')  # Display usage instructions if no file path is provided
        sys.exit(1)

# This is the main entry point of the program
main()  # Call the main function to execute the program

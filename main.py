from stats import get_book_wordcount  # Import the function to count words from stats module
from stats import get_book_lettercount  # Import the function to count letters from stats module
from stats import letter_count  # Import the letter count function from stats module
# Import necessary functions from stats module



def get_book_text(filepath): # Function to read the book text from a file
    with open(filepath) as f: # Open the file in read mode
        text = f.read() # Read the entire content of the file
    return text # Return the text read from the file

def main():
    filepath = 'books/frankenstein.txt'  # Path to the book file
    word_count = get_book_wordcount(filepath)  # Count the words in the book text
    print(f'{word_count} words found in the document')  # Display the word count
    testx=get_book_lettercount(filepath)  # Count the letters in the book text and display the count
    print(testx)

# This is the main entry point of the program
main()  # Call the main function to execute the program

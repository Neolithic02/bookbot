def get_book_wordcount(filepath): # Function to count the words in the book text
    with open(filepath) as f: # Open the file in read mode
        text = f.read() # Read the entire content of the file
        words = text.split()  # Split the text into words
        word_count = len(words)  # Count the number of words
    return word_count  # Return the word count

def letter_count(text):  # Function to count the letters in a given text
    count = {} # Initialize an empty dictionary to store letter counts
    for char in text:  # Iterate through each character in the text
        count[char] = count.get(char, 0) + 1  # Increment the count for each character
    return count  # Return the total letter count

def get_book_lettercount(filepath):  # Function to count the letters in the book text
    with open(filepath) as f:  # Open the file in read mode
        letter_count_value = {}  # Initialize an empty dictionary to store letter counts
        text = f.read()  # Read the entire content of the file
        text= text.lower()  # Convert the text to lowercase for uniformity
        letter_count_value = letter_count(text) # Call the letter_count function to count letters in the text
    return letter_count_value  # Return the letter count value

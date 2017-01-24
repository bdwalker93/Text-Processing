import re
from time import clock

# Reads input from the specified file and tokenizes all words into a map
def generateTokenFrequencyMap(file_name1: str) -> {str, int}:
    # Opens the specified file
    file = open(file_name1)

    # Stores all of the word frequencies in a map
    frequency_map = {}

    # We split on anything that is not a comma, letter (case sensitive), or apostrophe
    for line in file:
        for token in re.split('[^a-zA-Z0-9\']', line):

            # Multiple split chars in a row cause an empty token to be shown
            if token:
                if token.lower() in frequency_map:
                    frequency_map[token.lower()] += 1
                else:
                    frequency_map[token.lower()] = 1

    # Close the input stream
    file.close()

    return frequency_map

# Finds the number of same words between two documents
def determineIntersections(file_name2: str, frequency_map: {str, int}) -> int:
    # Total number of file intersections
    total_intersections = 0

    # Opens the specified file
    file = open(file_name2)

    # We split on anything that is not a comma, letter (case sensitive), or apostrophe
    for line in file:
        for token in re.split('[^a-zA-Z0-9\']', line):

            # Multiple split chars in a row cause an empty token to be shown
            if token:
                if token.lower() in frequency_map and frequency_map[token.lower()] > 0:
                    frequency_map[token.lower()] = -1
                    total_intersections += 1

                    # Prints the common tokens
                    print(token.lower())

    # Close the input stream
    file.close()

    return total_intersections

if __name__ == '__main__':

    # Starts the timer
    start = clock()

    print(determineIntersections("input2.txt", generateTokenFrequencyMap("input1.txt")))

    # Ends the timer
    end = clock()

    # Displays execution time
    print("Total Execution Time:", end - start, "sec")
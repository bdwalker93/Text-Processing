import re
import sys

# Reads input from the specified file and tokenizes all words into a map
def generateTokenFrequencyMap(file_name1: str) -> {str, int}:
     try:
        # Opens the specified file
        file = open(file_name1)

        # Stores all of the word frequencies in a map
        frequency_map = {}

        # We split on anything that is not a comma, letter (case sensitive), or apostrophe
        for line in file:
            for token in re.split('[^a-zA-Z0-9]', line):

                # Multiple split chars in a row cause an empty token to be shown
                if token:
                    if token.lower() not in frequency_map:
                        frequency_map[token.lower()] = 1

        # Close the input stream
        file.close()

        return frequency_map
     except:
         print("Error! The following file does not exist:", file_name1)


# Finds the number of same words between two documents
def determineIntersections(file_name2: str, frequency_map: {str, int}) -> int:
    # Total number of file intersections
    total_intersections = 0

    try:
        # Opens the specified file
        file = open(file_name2)

        # We split on anything that is not a comma, letter (case sensitive), or apostrophe
        for line in file:
            for token in re.split('[^a-zA-Z0-9\']', line):

                # Multiple split chars in a row cause an empty token to be shown
                if token:
                    if token.lower() in frequency_map:
                        del frequency_map[token.lower()]
                        total_intersections += 1

                        # Prints the common tokens
                        print(token.lower())

        # Close the input stream
        file.close()

        return total_intersections

    except:
        print("Error! The following file does not exist:", file_name2)
        raise

if __name__ == '__main__':

    # Argument counter
    count = 1

    # loops through all the input files
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("Pass 2 input file as command line argument!")
    else:
        try:
            print(determineIntersections(str(sys.argv[1]), generateTokenFrequencyMap(str(sys.argv[2]))))
        except:
            print("")
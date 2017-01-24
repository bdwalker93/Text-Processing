import re

# Reads input from the specified file and tokenizes all words within it
def tokenize(file_name: str) -> [str]:
    # Opens the specified file
    file = open(file_name)

    # Stores all of the words read in from the input file
    words =  {}

    # We split on anything that is not a comma, letter (case sensitive), or apostrophe
    for line in file:
        for token in re.split('[^a-zA-Z0-9\']', line):

            # Multiple split chars in a row cause an empty token to be shown
            if token:
                words.append(token.lower())



        print(len(words))

    # Close the input stream
    file.close()

    return words





if __name__ == '__main__':
    # printFrequencies(computeWordFrequencies(tokenize("C:\\Users\\Brett\\Desktop\\example2.txt")))
    printFrequencies(computeWordFrequencies(tokenize("smallExample.txt")))
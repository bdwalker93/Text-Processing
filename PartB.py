import re

# Reads input from the specified file and tokenizes all words within it
def generateTokenFrequencyMap(file_name: str) -> {str, int}:
    # Opens the specified file
    file = open(file_name)

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


# Prints word frequencies in decreasing order
def printFrequencies(frequency_map: {str, int}):
    for k in sorted(frequency_map, key=frequency_map.get, reverse=True):
        print(k, "->", frequency_map[k])

if __name__ == '__main__':
    # printFrequencies(computeWordFrequencies(tokenize("C:\\Users\\Brett\\Desktop\\example2.txt")))
    printFrequencies(generateTokenFrequencyMap("smallExample.txt"))
# Guided Exploration No. 3
# Owen Baker

# Imports everything from the random library
import random

# Declares an empty list that will be used later to store the rap names
possible_names = []

# Opens a new file to "write" which will store the new names generated in the code
outputFile = open('rap-names-output.txt', 'w')

# Opens rap-names.txt to "read" then assigns a handle to the dataFile file which is a variable.
with open('rap-names.txt', 'r') as dataFile:
    # Uses a for loop to iterate through each line in rap-names.txt one line at a time
    for name in dataFile:
        # Reads a line from rap-names.txt and then strips off the invisible line-feed at the end of each line. Then it appends the name to the possible_names list.
        possible_names.append(name.rstrip())

# Gets an integer input from the user asking how many rap names they want and assigns that the the variable count.
count = int(input('How many rap names would you like to create? '))
# Gets an integer input from the user asking how many parts their name should have and assigns it to the part variable.
parts = int(input('How many parts should the name contain? '))

# Iterates through the loop as many times as the user wanted when they entered how many names they would like to create.
for i in range(count):
    # Declares an empty list that will hold the rap name parts
    name_parts = []
    # Iterates for the number of rap names that the user wants as part of the names
    for j in range(parts):
        # Randomly selects names from the possible_names list and appends it to the name_parts list.
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

    # Takes the handle to the file where it writes out the generated rap names. Also Takes the name_parts list and glues them together with a space with a new line character being added to the string.
    outputFile.write(f"{' '.join(name_parts)}\n")
    # While the line above writes this statement to the file, this line prints it out on the terminal.
    print(f"{' '.join(name_parts)}")

# Closes the output file.
outputFile.close()

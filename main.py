
def read_file(path):
    with open(path, 'r') as file:  # opening the file
        contents = file.read()  # read all file as text (string)

        # to see each line as element of list we use
        # file.readlines()

        return contents  # return the contents

    
# File path
path = "chapter1.txt"
file_data = read_file(path)  # Calling the function

print(file_data)

# Reading file the second way using open only

file = open(path, 'r')  # Open file
contents = file.read()  # Read the file
print(contents)  # Printing the contents
file.close()  # close the file

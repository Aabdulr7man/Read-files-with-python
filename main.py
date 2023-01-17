
def read_file(path):
    with open(path, 'r') as file:
        contents = file.read()  # read all file as text (string)

        # to see each line as element of list we use
        # file.readlines()

        return contents


path = "chapter1.txt"
file_data = read_file(path)

# print(file_data)

# Reading file the other way

file = open(path, 'r')  # Open file
contents = file.read()  # Read the file
print(contents)  # Printing the contents
file.close()  # close the file


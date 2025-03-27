# Creating and writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text.\n")
    file.write("Writing multiple lines is easy.\n")

# Reading the file
with open("example.txt", "r") as file:
    content = file.read()

# Displaying the contents
print("File Contents:")
print(content)

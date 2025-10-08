import os
filename = "example.txt"
with open(filename, 'w') as file:
    file.write("Hello.\n")
    file.write("This is the file handling .\n")
print(f"File '{filename}' created and written.")

print("\nReading file contents:")
with open(filename, 'r') as file:
    content = file.read()
    print(content)                                         

with open(filename, 'a') as file:
    file.write("This line is appended.\n")
print(f"Data appended to '{filename}'.")

print("\nFile contents after appending:")
with open(filename, 'r') as file:
    print(file.read())

with open(filename, 'r') as file:
    lines = file.readlines()

lines[1] = "This line has been updated.\n"

with open(filename, 'w') as file:
    file.writelines(lines)
print(f"Data updated in '{filename}'.")

print("\nFile contents after update:")
with open(filename, 'r') as file:
    print(file.read())

with open(filename, 'w') as file:
    pass  
print(f"Contents of '{filename}' deleted.")


print("\nFile contents after deleting contents:")
with open(filename, 'r') as file:
    print(repr(file.read()))  

new_filename = "renamed_example.txt"
os.rename(filename, new_filename)
print(f"File renamed to '{new_filename}'.")

os.remove(new_filename)
print(f"File '{new_filename}' deleted.")

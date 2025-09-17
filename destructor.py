class FileHandler:
    def __init__(self, filename, mode='r'):
        """The constructor opens a file."""
        print(f"Opening file: '{filename}'")
        self.file = open(filename, mode)

    def write_to_file(self, data):
        """A method to write data."""
        self.file.write(data)

   
   
   
    def __del__(self):
        """The destructor closes the file."""
        if not self.file.closed:
            print(f"Closing file from destructor.")
            self.file.close()
file_obj = FileHandler("my_data.txt", 'w')
file_obj.write_to_file("Hello, this is a test.")
del file_obj
print("Program has finished.")

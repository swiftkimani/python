def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., convert all text to uppercase)
        modified_content = content.upper()  # Example modification
        
        # Open the output file in write mode
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"File modified and saved as '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for input and output file names
input_filename = input("Enter the name of the file to read: ")
output_filename = input("Enter the name of the new file to save the modified content: ")

# Call the function with user input
read_and_modify_file(input_filename, output_filename)

# file_read_write.py

def read_and_write_file(input_file, output_file):
    try:
        # Open input file in read mode
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Modify content (example: convert text to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File has been read from {input_file} and modified version saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    read_and_write_file("input.txt", "output.txt")
 
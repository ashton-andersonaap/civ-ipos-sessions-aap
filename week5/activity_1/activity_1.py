def main():
    # TODO Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal
    def text_to_bytes(string):
        return string.encode('utf-8')
    def bytes_to_text(bytes):
        return bytes.decode('utf-8')
    def integer_to_bytes(integer):
        return (integer).to_bytes(length=1, byteorder='big')
    def bytes_to_integer(bytes):
        return int.from_bytes(bytes, byteorder='big')


    # Main program logic
    # TODO Open the binary file for reading and create output text and bytes files for writing using the context manager
    try:
        with open('activity_1/data.bin','rb', encoding="utf-8") as file, \
             open('converted_text.txt', 'w', encoding="utf-8") as text_output,  \
             open('reversed_bytes.bin.', 'wb', encoding="utf-8") as bytes_output:
                # Iterate through each line in the binary file
                for line in file:
                    # TODO Decode the line to Unicode string and remove leading/trailing whitespaces
                    line = bytes_to_text(line).strip()
                    # Check if the line starts with "TEXT:"
                    if line.startswith("TEXT:"):
                        # Extract text content, convert to uppercase, and write to text file
                        text_to_print = line[5:].upper()
                        text_output.write(text_to_print + '\n')
                    
                    # Check if the line starts with "BYTES:"
                    elif line.startswith("BYTES:"):
                        print(line)

                        # TODO Extract the string and encode to hexadecimal
                        encoded_hex_data = line [6:].encode().hex()
                        # TODO Extract byte content, convert to bytes object(using fromhex()), 
                        bytes_data = bytes.fromhex(encoded_hex_data)
                        # Using your helper functions 
                        # TODO 1. reverse bytes, and write to bytes file

                        # TODO 2. convert back to text

                        # TODO 3. convert back to bytes

                        # Write the bytes data
                        bytes_output.write(bytes_data)
    # TODO use the in built IOError class                 
    except:
        pass
        # Handle file I/O errors
        # IOError - see definition, also Documentation: https://docs.python.org/3/library/io.html#
        # print(binary_error_message.strerror)

        # Handle other exceptions using the exception class
        
if __name__ == "__main__":
    main()
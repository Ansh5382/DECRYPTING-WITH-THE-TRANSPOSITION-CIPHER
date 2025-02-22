"""
    Decrypts a transposition cipher text using the given key.
    This function takes a ciphertext and a key, and decrypts the ciphertext by reversing the transposition cipher process. 
    The ciphertext is divided into columns based on the key, and then the plaintext is reconstructed by reading the columns in order.
    Args:
        ciphertext (str): The encrypted text to be decrypted.
        key (int): The number of columns used in the transposition cipher.
    Returns:
        str: The decrypted plaintext.
    """
def decrypt(ciphertext, key):
    # Calculate the number of columns and rows
    num_cols = key
    num_rows = len(ciphertext) // num_cols
    num_full_cols = len(ciphertext) % num_cols

    # Create a list of empty strings for each column
    columns = [''] * num_cols
    index = 0

    # Fill the columns with the ciphertext characters
    for i in range(num_cols):
        # Determine the length of the current column
        col_length = num_rows + (1 if i < num_full_cols else 0)
        # Assign the substring to the current column
        columns[i] = ciphertext[index:index + col_length]
        # Move the index to the next substring
        index += col_length

    # Create a string to hold the plaintext
    plaintext = ''
    
    # Read the columns in order to reconstruct the plaintext
    for i in range(num_rows + 1):  # +1 to handle the last row if it has extra characters
        for j in range(num_cols):
            # Append the character to the plaintext if it exists
            if i < len(columns[j]):
                plaintext += columns[j][i]

    return plaintext

def main():
    # Get the ciphertext and key from the user
    ciphertext = input("Enter the ciphertext: ")
    key = int(input("Enter the key: "))
    # Decrypt the ciphertext
    decrypted_text = decrypt(ciphertext, key)
    # Print the decrypted text
    print("Decrypted:", decrypted_text)

# Call the main function
main()
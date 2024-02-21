# List of lowercase English alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt(cipher_text, k):
    """
    Decrypts a given cipher text using a Caesar cipher with a specified key.

    Parameters:
    - cipher_text (str): The input text to be decrypted.
    - k (int): The decryption key representing the shift in the alphabet.

    Returns:
    - str: The decrypted plain text.
    """
    # Remove spaces from the input cipher text and convert it to lowercase
    cipher_text_no_space = cipher_text.replace(" ", "")
    cipher_text_list = list(cipher_text_no_space.lower())
    plain_text = []

    # Iterate through each character in the cipher text
    for i in range(len(cipher_text_list)):
        # Find the position of the current character in the alphabet
        current_alpha_pos = alphabets.index(cipher_text_list[i])
        # Calculate the final position after applying the Caesar cipher in reverse
        final_count = current_alpha_pos - k

        # Check if the final position is before 'a' (index 0)
        if final_count < 0:
            # Wrap around the alphabet if the final position is before 'a'
            plain_text.append(alphabets[26 + final_count])
        else:
            # Append the decrypted character to the plain text
            plain_text.append(alphabets[final_count])

    # Convert the list of decrypted characters to a string and return it
    plain_text = ''.join(plain_text)
    return plain_text

# Example usage
# decrypted_text = decrypt("sxjsavlgewkkmhzakmhyjsvw", 18)
# print("Decrypted Text:", decrypted_text)

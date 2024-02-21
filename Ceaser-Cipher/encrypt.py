# List of lowercase English alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, k):
    """
    Encrypts a given plain text using a Caesar cipher with a specified key.

    Parameters:
    - plain_text (str): The input text to be encrypted.
    - k (int): The encryption key representing the shift in the alphabet.

    Returns:
    - str: The encrypted cipher text.
    """
    # Remove spaces from the input text and convert it to lowercase
    plain_text_no_space = plain_text.replace(" ", "")
    plain_text_list = list(plain_text_no_space.lower())
    cipher_text = []

    # Iterate through each character in the input text
    for i in range(len(plain_text_list)):
        # Find the position of the current character in the alphabet
        current_alpha_pos = alphabets.index(plain_text_list[i])
        # Calculate the final position after applying the Caesar cipher
        final_count = k + current_alpha_pos

        # Check if the final position is beyond 'z' (index 25)
        if final_count > 25:
            # Wrap around the alphabet if the final position exceeds 'z'
            cipher_text.append(alphabets[(final_count - 25) - 1])
        else:
            # Append the encrypted character to the cipher text
            cipher_text.append(alphabets[k + current_alpha_pos])

    # Convert the list of encrypted characters to a string and return it
    cipher_text = ''.join(cipher_text)
    return cipher_text

# Example usage
# print(encrypt("Afraid to Mess Up His Upgrade", 18))

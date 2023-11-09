def encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():  # If the character is an uppercase letter
            new_char = chr(((ord(char) - 65 + shift) % 26) + 65)
        else:  # If the character is a lowercase letter
            new_char = chr(((ord(char) - 97 + shift) % 26) + 97)

        encrypted_text += new_char  # Add the new character to the encrypted text

    return encrypted_text

# Example usage
text = "HELLOWORLD"
shift = 1
print("Original Text: " + text)
print("Shift Amount : " + str(shift))
print("Encrypted Text: " + encrypt(text, shift))

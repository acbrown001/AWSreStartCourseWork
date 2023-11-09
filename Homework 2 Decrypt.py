def decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isupper():
            new_char = chr(((ord(char) - 65 - shift) % 26) + 65)
        else:
            new_char = chr(((ord(char) - 97 - shift) % 26) + 97)

        decrypted_text += new_char

    return decrypted_text

# Example usage
encrypted_text = "IFMMPXPSME"
shift = 1
print("Encrypted Text: " + encrypted_text)
print("Shift Amount : " + str(shift))
print("Decrypted Text: " + decrypt(encrypted_text, shift))
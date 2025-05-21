class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                # Get the shift value from the key character
                # Convert key character to uppercase to handle mixed-case keys consistently
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    # Encrypt uppercase letters
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    # Encrypt lowercase letters
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                key_index += 1  # Move to the next key character only for alphabetic characters
            else:
                # Append non-alphabetic characters as they are
                encrypted_text += char
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                # Get the shift value from the key character
                # Convert key character to uppercase
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    # Decrypt uppercase letters
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    # Decrypt lowercase letters
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
                key_index += 1  # Move to the next key character only for alphabetic characters
            else:
                # Append non-alphabetic characters as they are
                decrypted_text += char
        return decrypted_text
def vigenere_encrypt(message, key):
    encrypted_message = ""
    key_length = len(key)
    for i, char in enumerate(message):
        if char.isalpha():
            key_char = key[i % key_length].lower()
            shift = ord(key_char) - ord('a')
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ""
    key_length = len(key)
    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            key_char = key[i % key_length].lower()
            shift = ord(key_char) - ord('a')
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

# Accepting a text file containing a message
input_file_path = input("You may now input the path where your text file is located: ")
with open(input_file_path, 'r') as file:
    message = file.read()

# Encrypting the message using the Vigenère cipher
key = input("Your Encryption Key: ")
encoded_message = vigenere_encrypt(message, key)

# Saving the encrypted message to a text file
encoded_file_path = input("You may now input the path you want to save the encrypted text file: ")
with open(encoded_file_path, 'w') as file:
    file.write(encoded_message)

# Accepting the encrypted text file
encoded_file_path = input("You may now input the path you created that store the encrypted text file: ")
with open(encoded_file_path, 'r') as file:
    encoded_message = file.read()

# Decrypting the message using the Vigenère cipher
key = input("Your Decryption key (It should be the same as the encryption key): ")
decoded_message = vigenere_decrypt(encoded_message, key)

# Saving the decrypted message to a text file
decoded_file_path = input("You may now input the path you want to save the decrypted text file: ")
with open(decoded_file_path, 'w') as file:
    file.write(decoded_message)

print("Decrypting completed and saved to", decoded_file_path)
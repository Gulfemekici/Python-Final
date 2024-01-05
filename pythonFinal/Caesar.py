import pyperclip


def caesar_cipher(text, key, mode):
    result = ''  # Initialize an empty string to store the encrypted/decrypted text

    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Determine the ASCII shift based on whether the character is uppercase or lowercase
            shift = 65 if char.isupper() else 97

            # Apply the Caesar cipher encryption or decryption formula
            # For encryption (mode='e'): shift the character to the right by the key
            # For decryption (mode='d'): shift the character to the left by the key
            result += chr((ord(char) - shift + key) % 26 + shift) if mode == 'e' else chr(
                (ord(char) - shift - key) % 26 + shift)
        else:
            # If the character is not an alphabet letter, leave it unchanged
            result += char

    return result


def main():
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    choice = input("> ").lower()

    # Validate user input
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return

    # Get the encryption/decryption key from the user
    key = int(input("Please enter the key (0 to 25) to use.\n> "))

    # Validate the key
    if not 0 <= key <= 25:
        print("Invalid key. Please enter a key between 0 and 25.")
        return

    # Get the message from the user
    message = input("Enter the message to {}.\n> ".format("encrypt" if choice == 'e' else "decrypt"))

    # Perform the encryption or decryption
    result = caesar_cipher(message, key, choice)

    # Display the result
    print(result)

    # Copy the result to the clipboard for easy use
    pyperclip.copy(result)
    print("Full {}ed text copied to clipboard.".format("encrypt" if choice == 'e' else "decrypt"))


if __name__ == "__main__":
    main()

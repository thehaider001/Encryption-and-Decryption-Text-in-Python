def caesar_cipher(text, shift, operation):
    result = ""
    if operation == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
            
    return result

def main():
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

    if operation not in ['encrypt', 'decrypt']:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
        return
    
    result = caesar_cipher(text, shift, operation)
    
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()

# Caesar Cipher

A Python implementation of the classic Caesar Cipher encryption and decryption algorithm. This project demonstrates fundamental cryptography concepts while providing an interactive command-line interface.

## 🎯 Project Overview

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in the alphabet by a fixed number of positions. For example, with a shift of 3:
- 'A' becomes 'D'
- 'B' becomes 'E'
- 'X' becomes 'A' (wrapping around)

## ✨ Features

- **Encode/Decode**: Encrypt messages or decrypt previously encrypted messages
- **Custom Shift**: Choose any shift value (automatically handles shifts > 26)
- **Character Preservation**: Keeps numbers, symbols, and spaces unchanged
- **Interactive Interface**: User-friendly command-line interface with ASCII art
- **Restart Capability**: Continue using the program without restarting

## 🚀 How to Use

1. **Run the program**:
   ```bash
   python ceaser-cipher.py
   ```

2. **Choose operation**:
   - Type `encode` to encrypt a message
   - Type `decode` to decrypt a message

3. **Enter your message**:
   - Type any text (letters, numbers, symbols, spaces)
   - The program will automatically convert to lowercase

4. **Set the shift value**:
   - Enter any integer (positive or negative)
   - The program automatically handles shifts greater than 26

5. **View results**:
   - The encrypted/decrypted message will be displayed

6. **Continue or exit**:
   - Type `yes` to encrypt/decrypt another message
   - Type `no` to exit the program

## 📝 Example Usage

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
Hello World! 123
Type the shift number:
3
Here's the encoded result: khoor zruog! 123

Do you want to restart the cipher program? 
Type 'yes' if you want to go again. Otherwise type 'no'. : no
GoodBye
```

## 🔧 Technical Details

### Algorithm
- Uses a 52-character alphabet array (a-z repeated twice) for easy wrapping
- Handles shifts greater than 26 using modulo operation (`shift % 26`)
- Preserves non-alphabetic characters (numbers, symbols, spaces)
- Converts all input to lowercase for consistency

### Key Functions
- `caesar(start_text, shift_amount, cipher_direction)`: Main encryption/decryption function
- ASCII art logo imported from `art.py` for visual appeal

### Error Handling
- Automatically handles shift values greater than 26
- Preserves special characters and spaces
- Input validation for shift numbers

## 📁 Project Structure

```
day-8-ceaser-cipher/
├── ceaser-cipher.py    # Main program file
├── art.py             # ASCII art logo
└── README.md          # This file
```

## 🎓 Learning Objectives

This project demonstrates:
- **String manipulation** and character processing
- **Modulo arithmetic** for handling large shift values
- **Control flow** with loops and conditionals
- **Function design** and parameter handling
- **User input processing** and validation
- **ASCII art integration** for enhanced user experience

## 🔐 Security Note

⚠️ **Important**: The Caesar Cipher is a historical encryption method and is **not secure** for modern applications. It's easily breakable through frequency analysis and brute force attacks. This project is intended for educational purposes only.

## 🛠️ Requirements

- Python 3.x
- No external dependencies required

## 📚 Further Reading

- [Caesar Cipher on Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Cryptography Basics](https://en.wikipedia.org/wiki/Cryptography)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

---

*This project is part of a Python learning journey, focusing on fundamental programming concepts through practical cryptography implementation.*

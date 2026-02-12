from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}

# Create reverse dictionary for decoding
morse_to_text = {v: k for k, v in morse_code.items()}


def text_to_morse(text):
    """Convert text to morse code"""
    morse_result = []
    for char in text.lower():
        if char in morse_code:
            morse_result.append(morse_code[char])
        else:
            morse_result.append(char)
    return " ".join(morse_result)


def morse_to_text_converter(morse):
    """Convert morse code to text"""
    # Split by spaces to get individual morse characters
    morse_chars = morse.strip().split(" ")
    text_result = []
    
    for morse_char in morse_chars:
        if morse_char in morse_to_text:
            text_result.append(morse_to_text[morse_char])
        elif morse_char == "":
            continue
        else:
            text_result.append("?")
    
    return "".join(text_result)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    input_text = data.get('text', '')
    mode = data.get('mode', 'encode')
    
    if mode == 'encode':
        result = text_to_morse(input_text)
    else:
        result = morse_to_text_converter(input_text)
    
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)

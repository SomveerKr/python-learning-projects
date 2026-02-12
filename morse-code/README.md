# Morse Code Converter

A web-based application built with **Flask** that converts text into Morse code and vice versa. This project is part of the **100 Days of Code** challenge.

## Features

- **Text to Morse Code**: Convert any alphanumeric text (including basic punctuation) into Morse code.
- **Morse to Text Decoding**: Decode Morse code back into readable text.
- **Real-time Conversion**: Seamlessly switch between encoding and decoding modes.
- **Support for Special Characters**: Handles numbers, punctuation marks, and basic symbols.
- **One-Click Copy**: Easily copy the conversion result to your clipboard.

## Technologies Used

- **Python**: Core logic for Morse code conversion.
- **Flask**: Web framework for handling server-side logic and routing.
- **HTML/CSS/JavaScript**: Frontend for the user interface, styling, and client-side interactions.

## Project Structure

```
day-82-morse-code/
├── app.py              # Main Flask application file
├── requirements.txt    # List of dependencie
├── static/
│   ├── style.css       # CSS styles
│   └── script.js       # Client-side JavaScript logic
└── templates/
    └── index.html      # HTML template
```

## Setup and Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd morse-code
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    
    # Windows
    venv\Scripts\activate
    
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application**:
    ```bash
    python app.py
    ```

5.  **Open in Browser**:
    Visit `http://127.0.0.1:5000/` in your web browser.

## Usage

1.  **Select Mode**: Choose between "Text to Morse" or "Morse to Text".
2.  **Input Text**: 
    - For **Text to Morse**: Type any text.
    - For **Morse to Text**: Enter Morse code with spaces between characters. Use `/` for word spaces.
      - Example: `.... . .-.. .-.. --- / .-- --- .-. .-.. -..` translates to `HELLO WORLD`.
3.  **Convert**: Click the **Convert** button to see the result.
4.  **Copy**: Use the **Copy** button to copy the output to your clipboard.

## License

This project is open source and available under the [MIT License](LICENSE).

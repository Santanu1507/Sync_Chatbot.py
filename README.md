# Chatbot

Chatbot is a Python-based chatbot that allows users to interact with it through both text and voice input. The chatbot provides responses to various user queries and can perform basic conversation tasks.

## Features

- Text-based interaction: Users can type in their queries in the chat area and receive responses from the chatbot.
- Voice-based interaction: Users can click the "Speak" button and speak their queries, and the chatbot will process the voice input and respond accordingly.
- Dynamic Responses: The chatbot has pre-defined responses for specific keywords like greetings, jokes, and more. It also uses fuzzy matching to provide relevant responses even for variations of keywords.
- Graphical User Interface: The chatbot comes with a simple and user-friendly GUI built using the Tkinter library.

## Requirements

- Python 3.x
- Tkinter library (usually comes pre-installed with Python)
- tkinter Scrollbar (part of the tkinter package)
- fuzzywuzzy library (for fuzzy string matching)
- speech_recognition library (for processing voice input)
- pyperclip library (for copying the chatbot's response to the clipboard)

## Usage

1. Run the `chatbot.py` file to start the application.
2. Use the text input field to type in your queries and click the "Send" button to get responses.
3. Alternatively, click the "Speak" button and use your microphone to speak your queries for voice-based interaction.

## How It Works

- The chatbot GUI is created using the Tkinter library, providing a chat area, input field, and buttons for text and voice input.
- The `fuzzywuzzy` library is used to perform fuzzy string matching to find the closest matching keyword for generating responses based on user input.
- The `speech_recognition` library enables voice input processing. The chatbot listens to user voice input, converts it to text, and responds accordingly.
- The chatbot provides a set of pre-defined responses for specific keywords, and it falls back to a default response if the input doesn't match any keywords.

## Future Improvements

- Expand the chatbot's functionality by integrating APIs for tasks like weather, news, or online search.
- Implement natural language processing (NLP) to improve understanding and response generation.
- Add user context tracking to provide more personalized responses.

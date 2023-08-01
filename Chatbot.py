import tkinter as tk
from tkinter import Scrollbar
from fuzzywuzzy import fuzz
import speech_recognition as sr
import threading
import subprocess
import random

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Zappy Chatbot")
        
        # Create and configure the widgets for the chatbot GUI
        self.create_widgets()
        
        # Define a dictionary of responses for different user inputs
        self.responses = {
            "hello": ["Hello! How can I assist you?", "Hi there! How may I help you?", "Hey! What can I do for you?"],
            "how are you": ["I'm just a chatbot, but thanks for asking!", "I don't have feelings, but I'm here to assist you!"],
            "bye": ["Goodbye! Have a great day!", "Take care and see you later!", "Farewell! Come back anytime!"],
            "name": ["I'm just a chatbot, I don't have a name.", "Names are for humans, I'm your friendly chatbot!"],
            "age": ["I'm an AI chatbot, so I don't have an age.", "Age doesn't apply to me, I'm always learning!"],
            "weather": ["I'm sorry, I don't have access to real-time weather information.", "Unfortunately, I can't check the weather."],
            "joke": ["Why don't scientists trust atoms? Because they make up everything!", 
                     "Here's a joke for you: Why did the scarecrow win an award? Because he was outstanding in his field!"],
            "thanks": ["You're welcome!", "No problem, happy to assist!", "You got it!", "Anytime!"],
            "default": ["I'm sorry, but I don't understand that. Could you please rephrase?", 
                        "I'm not sure what you mean. Could you try asking in a different way?"]
        }       
        self.init_voice_assistant()

    def create_widgets(self):
        # Create and configure the chat area (a Text widget) where the conversation is displayed
        self.chat_area = tk.Text(self.root, height=10, width=50, wrap="word", font=("Comic Sans MS", 12))
        self.chat_area.pack(padx=10, pady=10)

        # Create and configure a scrollbar for the chat area
        self.scrollbar = Scrollbar(self.root, command=self.chat_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the chat area to use the scrollbar
        self.chat_area.config(yscrollcommand=self.scrollbar.set)

        # Create an entry field for user input
        self.message_entry = tk.Entry(self.root, width=40, font=("Comic Sans MS", 12))
        self.message_entry.pack(padx=10, pady=5)

        # Create a "Send" button to process user input
        self.send_button = tk.Button(self.root, text="Send", command=self.process_message, font=("Comic Sans MS", 12, "bold"), bg="blue", activebackground="lightblue")
        self.send_button.pack(pady=10)

        # Create a "Speak" button to process voice input
        self.voice_button = tk.Button(self.root, text="Speak", command=self.process_voice_input, font=("Comic Sans MS", 12, "bold"), bg="green", activebackground="lightgreen")
        self.voice_button.pack(pady=5)

        self.is_listening = False

    def process_message(self):
        # Function to process user's text input and get a response from the chatbot
        user_input = self.message_entry.get().lower()
        self.chat_area.insert(tk.END, "You: " + user_input + "\n")
        self.message_entry.delete(0, tk.END)

        response = self.get_response(user_input)
        self.chat_area.insert(tk.END, "Zappy: " + response + "\n")

    def process_voice_input(self):
        # Function to handle the "Speak" button click event for voice input
        self.voice_button.config(state=tk.DISABLED)

        voice_thread = threading.Thread(target=self.process_voice_input_thread)
        voice_thread.start()

    def process_voice_input_thread(self):
        # Function to process voice input using a separate thread to avoid blocking the main GUI thread
        self.is_listening = True

        user_input = self.get_voice_input()

        self.is_listening = False

        self.voice_button.config(state=tk.NORMAL)

        if user_input:
            self.message_entry.delete(0, tk.END)
            self.message_entry.insert(tk.END, user_input)
            self.process_message()

    def init_voice_assistant(self):
        # Initialize the speech recognizer for voice input
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        # Function to speak the given text using a text-to-speech tool
        subprocess.Popen(["python", "text_to_speech.py", text], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def get_response(self, user_input):
        # Function to get an appropriate response from the chatbot based on user input
        highest_similarity = 0
        matched_keyword = ""

        # Find the most similar keyword from the user input
        for keyword in self.responses.keys():
            similarity = fuzz.partial_ratio(user_input, keyword)
            if similarity > highest_similarity:
                highest_similarity = similarity
                matched_keyword = keyword

        # Return a response based on the matched keyword
        if highest_similarity >= 50:  
            return random.choice(self.responses[matched_keyword])
        else:
            return random.choice(self.responses["default"])

    def get_voice_input(self):
        # Function to get voice input from the user using the microphone
        with sr.Microphone() as source:
            if not self.is_listening:
                self.is_listening = True

                # Start a thread to speak the "Listening..." message while waiting for voice input
                t = threading.Thread(target=self.speak, args=("Listening... Please speak.",))
                t.start()

                # Adjust for ambient noise and listen for voice input
                self.recognizer.adjust_for_ambient_noise(source)

                try:
                    audio = self.recognizer.listen(source, timeout=5)
                    recognized_text = self.recognizer.recognize_google(audio).lower()

                    self.is_listening = False

                    return recognized_text
                except sr.UnknownValueError:
                    # If speech recognition fails to understand the input
                    self.speak("Sorry, I couldn't understand what you said.")
                    return ""
                except sr.RequestError:
                    # If there is an issue with the speech recognition service
                    self.speak("Sorry, there was an issue connecting to the speech recognition service.")
                    return ""
            else:
                return ""

if __name__ == "__main__":
    # Main entry point of the application
    root = tk.Tk()
    chatbot = ChatbotGUI(root)
    root.mainloop()

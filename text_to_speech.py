# Import the pyttsx3 library for text-to-speech functionality
import pyttsx3
# Import the sys module to access command-line arguments
import sys

# Get the text to be spoken from the command-line arguments
# The text should be passed as an argument when running the script
text = sys.argv[1]

# Initialize the pyttsx3 engine for text-to-speech
engine = pyttsx3.init()

# Set the speech rate (speed) to 150 words per minute
engine.setProperty('rate', 150)

# Use the engine to say the provided text
engine.say(text)

# Wait for the speech to finish before exiting the script
engine.runAndWait()

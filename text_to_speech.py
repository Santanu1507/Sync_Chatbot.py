import pyttsx3
import sys

text = sys.argv[1]

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say(text)
engine.runAndWait()

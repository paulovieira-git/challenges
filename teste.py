import speech_recognition as sr
from time import sleep
import keyboard  # pip install keyboard


r = sr.Recognizer()

with mic as source:
    # wait for a second to let the recognizer
    # adjust the energy threshold based on
    # the surrounding noise level
    r.adjust_for_ambient_noise(source, duration=0.2)
    input(" == START TALKING. (1 seconds). Say \'Thank you\' to Exit and generate log ==")
    # listens for the user's input
    audio = r.listen(source=source)
print('== Capture finished ==')
# Using google to recognize audio
transcript = r.recognize_google(audio)
print(transcript)
# transcript = transcript.lower()


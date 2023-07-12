
# -------------------------------------------------------Method Two--------------------------------------------------

import pyttsx3

myText=  input("Enter the text\n")
language ="en"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(myText)
engine.runAndWait()
# ----------------------------------------------------------End------------------------------------------------------

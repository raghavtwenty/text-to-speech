'''
Application Name: Text To Speech
Author : Raghav, Kendriya Vidyalaya, Coimbatore. [2021]
Github ID : @raghavtwenty
Created On: July 11, 2021 | Last Modified On: July 11, 2021
Version Info: 1.0
'''


# importing the required modules
import pyttsx3

# initialize the imported module
speech = pyttsx3.init()

# get the input 
strin = str(input("Type Here : "))
speech1 = pyttsx3.init()

# convert the text input to speech
speech1.say(strin)
speech1.runAndWait()
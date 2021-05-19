import eventhandler
import speech_recognition as sr
import eventhandler as ev
import winsound as sound
from playsound import playsound
import os
import time
from gtts import gTTS

class talker:

    def __init__(self):
        self.__recognizer =  sr.Recognizer()


    def __listen(self):
        with sr.Microphone() as source:
            print("\n")
            audio_text = self.__recognizer.listen(source)
            print("Time over, thanks")
            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            newString = ""




#Program starts here
if __name__ == '__main__':
    print()




    # try:
    #     # using google speech recognition
    #     newString = r.recognize_google(audio_text)
    #     print(newString)
    # except:
    #     print("Sorry, I did not get that")
    #
    # myobj = gTTS(text=newString, lang = "en", slow=False)
    # myobj.save("welcome.mp3")
    # os.system("welcome.mp3")

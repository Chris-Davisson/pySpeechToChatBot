import speech_recognition as sr


class Listen:

    def __init__(self):
        self.__recognizer = sr.Recognizer()

    def __listen(self):
        with sr.Microphone() as source:
            print("\n")
            audio_text = self.__recognizer.listen(source)
            print("Time over, thanks")
            newString = ""

import speech_recognition as sr
import translators
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio=r.listen(source)
    txt=r.recognize_google(audio)
    google=translators.google(txt,from_lang='en',to_lang='es')
    bing=translators.bing(txt,from_lang='en',to_lang='es')
    print(google)
    print(bing)
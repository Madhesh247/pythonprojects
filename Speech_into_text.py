import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    r.adjust_for_ambient_noise(source, duration=2)
    audio = r.listen(source)

try:
    text = r.recognize_sphinx(audio)   # OFFLINE
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio")
except sr.RequestError as e:
    print("Recognition error:", e)

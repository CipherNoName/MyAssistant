import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[102].id)

def saida_voz(texto):
    engine.say(texto)
    engine.runAndWait()
import speech_recognition as sr

def ouvir_fala(lingua): #defina um valor para sua lingua exenplo: lingua="pt-BR"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Fale sua pegunta: ")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language=lingua)
        return texto
    except sr.UnknownValueError:
        return "Não entendi o que você falou"
    except sr.RequestError as e:
        return f"Erro no serviço de reconhecimento: {e}"  # noqa: F706

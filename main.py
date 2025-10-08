# --------------------------------------------- EL PYTHONCITO XD 🐍🐍🐍🐍!!!!
# ------------ Convertir Voz a Texto

import speech_recognition as sr

# Crear un reconocedor
r = sr.Recognizer()


def transcription():
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        # Usar el motor de Google para reconocer
        text = r.recognize_google(audio, language="es-ES")
        print("✅🧠✅🧠✅ ", text)

        # Guardar la transcripción en 
        with open("py_transcription.txt", mode="a", encoding="utf-8") as file:
            file.write(text + "\n")

        # Si el usuario dice "salir" el programa finaliza
        if text.lower().strip() == "salir":
            print("\n👋 Saliendo del programa...\nVuelve pronto...")
            return False  # Salir del bucle
        return True  # Continuar escuchando

    except sr.UnknownValueError:
        print("\nNo entendí lo que dijiste 😅")
        return True
    except sr.RequestError:
        print("\nError al conectar con el servicio de reconocimiento🛜")
        return True

print("\n🎙️🎙️ Di algo, el Pythoncito te está escuchando ... 🎙️🎙️")

while True:
    if not transcription():
        break


print("\nJust keep going!!!")
print("El Pythoncito XD 🐍!")

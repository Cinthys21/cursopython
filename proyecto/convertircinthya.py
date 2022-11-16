from gtts import gTTS
import os
saludo = "Hola soy cinthya mi mision es convertir el texto a voz"
language = 'es-us'
speech = gTTS(text = saludo, lang = language, slow = False)
speech.save("texto.mp3")
os.system("start texto.mp3")
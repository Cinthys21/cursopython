# aplicado en quechua ahora:
from gtts import gTTS
import os
saludo = "Sutiymi cinthya, imay sutiqui?"
language = 'es-us'
speech = gTTS(text = saludo, lang = language, slow = False)
speech.save("quechua.mp3")
os.system("start texto.mp3")
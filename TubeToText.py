import pytube #Pytube es una libreria que nos permite descargar videos de youtube
import whisper #Wisper es un modelo de IA que nos permite crear un modelo de voz a partir de un texto

#Creamos una variable con nuestro link de youtube
yt_link = 'https://www.youtube.com/watch?v=xT75e-G1eak&list=PPSV' #Reemplazar por input de usuario

#Creamos una variable con el modelo de whisper
model = whisper.load_model('small')

#Creamos una variable con el video de youtube
yt_video = pytube.YouTube(yt_link)

#Creamos una variable con el audio del video de youtube
yt_audio = yt_video.streams.get_audio_only()

#Descargamos el audio del video de youtube
yt_audio.download(filename='audioYT.mp4')

#Creamos una variable donde guardaremos los resultados de nuestro modelo de whisper
result = model.transcribe('audioYT.mp4', fp16=False) # Agregar Utf-8 o latin-1 si hay problemas de codificación

#Imprimimos los resultados de nuestro modelo de whisper
print(result['text']) # Una vez que tengamos el texto lo enviamos a darle formato, negrita, cursiva, etc.


#El video tarda 122.3 seg en descargarse y 0.5 seg en transcribirse con el modelo de whisper small en una computadora con las siguientes caracteristicas: 
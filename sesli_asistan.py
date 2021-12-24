import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import requests 
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

r = sr.Recognizer()

def record(ask = False):
    if ask:
        speak(ask)
        print(ask)
    with sr.Microphone() as source:
        audio = r.listen(source)
        print('ses alındı lütfen işlenmesi için bekleyiniz')
        voice = ''
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
            print('anlayamadım')
        except sr.RequestError:
            speak('sistem çalışmıyor')
            print('sistem çalışmıyor')
        return voice

def response(voice):
    
    if 'nasılsın' in voice:
        speak('iyi senden')
        print('iyi senden')
        
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
        print(datetime.now().strftime('%H:%M:%S'))
        
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsun')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + ' için bulduğum sonuçlar')
        print(search + ' için bulduğum sonuçlar')
        
    if 'teşekkür'  in voice:
        speak('rica ederim')

    if 'hava durumu' in voice:
        hava = 'https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx#/'
        webbrowser.get().open(hava)
        speak('hava durumu sonuçları')
        print('hava durumu sonuçları')

    if 'YouTube' in voice:
        search = record('ne dinlemek istersin')
        youtube = 'https://youtube.com/search?q='+search
        webbrowser.get().open(youtube)
        speak(search + 'için bulunanlar')
        print(search + 'için bulunanlar')
        
    if 'Programı kapat' in voice:
        speak('görüşürüz')
        print('görüşürüz')     
        exit()


def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    time.sleep(5)
    playsound(file)
    os.remove(file)
    
speak('nasıl yardımcı olabilirim')
print('nasıl yardımcı olabilirim')
time.sleep(1)

while 1:
    voice = record()
    print(voice)
    response(voice)

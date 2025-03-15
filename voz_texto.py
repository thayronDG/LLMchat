import speech_recognition as sr
from time import sleep

def listar_microfones():
    microfones = sr.Microphone.list_microphone_names()
    for i, microfone in enumerate(microfones):
        print(f"Microfone {i}: {microfone}")

def ouvir_microfone():
    print("Estou te ouvindo...")
    microfone = sr.Recognizer()
    # listar_microfones()
    
    with sr.Microphone(1) as source: 
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        # sleep(2)
        audio = microfone.listen(source) # phrase_time_limit=3
        print('capturou')
        try:
            frase = microfone.recognize_google(audio, language='pt-BR') # language='pt-BR'
            print("Você disse: " + frase)
        except sr.UnknownValueError:
            print("Não entendi o que você disse")
            
        return(frase)
    

if __name__ == '__main__':
    ouvir_microfone()

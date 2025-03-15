import pyttsx3


def texto_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

if __name__ == '__main__':
    texto = input('Digite o texto: ')
    while texto != 'sair':
        texto_voz(texto)
        texto = input('Digite o texto: ')
        
        


# def listar_vozes():
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     for index, voice in enumerate(voices):
#         print(f"Voice {index}:")
#         print(f" - ID: {voice.id}")
#         print(f" - Name: {voice.name}")
#         print(f" - Languages: {voice.languages}")
#         print(f" - Gender: {voice.gender}")
#         print(f" - Age: {voice.age}")
#         print("\n")

# listar_vozes()


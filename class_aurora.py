# Description: This script is a simple chatbot that interacts with the user by asking questions and providing answers using a chatbot.
# https://www.youtube.com/watch?v=p1mD3aYb2iw
# https://github.com/ollama/ollama

'''
+-------------------+        +-----------------------+        +------------------+        +------------------------+
|   Step 1: Install |        |  Step 2: Real-Time    |        |  Step 3: Pass    |        |  Step 4: Live Audio    |
|   Python Libraries|        |  Transcription with   |        |  Real-Time       |        |       Stream from      |
+-------------------+        |   SpeechRecognition   |        |  Transcript to   |        |         pyttsx3        |
|                   |        +-----------------------+        |      LLAMA 3     |        +------------------------+
| - SpeechRecognition                    |                    +------------------+                    |
| - ollama          |                    |                             |                              |
| - pyttsx3         |                    v                             v                              v
| - pandas          |        +-----------------------+        +------------------+        +------------------------+
| - langchain       |        |                       |        |                  |        |                        |
+-------------------+        |      performs         |--------> LLAMA 3 generates|-------->  Pyttsx3 streams       |
                             |  real-time speech-to- |        |  response based  |        |  response as live      |
                             |  text transcription   |        |  on transcription|        |  audio to the user     |
                             |                       |        |                  |        |                        |
                             +-----------------------+        +------------------+        +------------------------+
                             
'''

import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3 or (elevenlabs)
import ollama
import os
import pandas as pd

class AuRoRa():
    def __init__(self):
        self.mensagens = [{"role": "system", "content": "Você é uma assistente virtual para aplicações de inteligência artificial e seu nome é AuRoRa. E meu nome é Thayron!"}]
        self.sem_palavra_ativadora = True
        self.entrada_por_texto = True
        self.falar = False
        if self.entrada_por_texto:
            self.sem_palavra_ativadora = True
        # ollama.api_key = os.getenv('OLLAMA_API_KEY') 

    def chatbot(self, messages):
        """
        A function that interacts with the Ollama chatbot to generate a response based on the given messages.
        """
        # for part in ollama.chat(model='llama3.1', messages=messages, stream=True):
        #     print(part['message']['content'], end='', flush=True)
            
        response = ollama.chat('llama3.1', messages=messages)
        return response['message']['content']


    def texto_voz(self, texto, voz_id):
        """
        Converts the given text to speech using the specified voice ID.
        """
        engine = pyttsx3.init()
        if voz_id is not None:
            engine.setProperty('voice', voz_id)
        engine.say(texto)
        engine.runAndWait()

    def ouvir_microfone(self):
        """
        Função responsável por capturar áudio do microfone e realizar o reconhecimento de fala.
        """
        print("Microfone iniciado...")
        microfone = sr.Recognizer()
        
        with sr.Microphone(1) as source: 
            microfone.adjust_for_ambient_noise(source)
            print("Diga alguma coisa (sair): ")
            audio = microfone.listen(source)
            print('capturou')
            try:
                frase = microfone.recognize_google(audio, language='pt-BR')
                print("-> Você disse: " + frase)
            except sr.UnknownValueError:
                print("Não entendi o que você disse")
                frase = ""
            return frase

    def main(self):
        """
        This function represents the main entry point of the program.
        It interacts with the user by asking questions and providing answers using a chatbot.
        """
        print("AuRoRa iniciada...\n")
        
        while True:
            question = ""
            
            if self.entrada_por_texto:
                question = input("-> Perguntar para AuRoRa (\"sair\"): ")
                if question.lower() == "sair":
                    print("\nSaindo.\n")
                    break
                self.mensagens.append({"role": "user", "content": str(question)})
                answer = self.chatbot(self.mensagens)
                self.mensagens.append({"role": "assistant", "content": answer})
                print("\n-> AuRoRa:", answer)
                print()
                if self.falar:
                    self.texto_voz(answer, voz_id=None)
            else:
                question = self.ouvir_microfone()
                if question.lower() == "sair":
                    print("\nSaindo\n")
                    break
                elif question == "":
                    print("\nSem captura de áudio\n")
                    continue
                else:
                    self.mensagens.append({"role": "user", "content": str(question)})
                    answer = self.chatbot(self.mensagens)
                    self.mensagens.append({"role": "assistant", "content": answer})
                    print("\n-> AuRoRa:", answer)
                    print()
                    if self.falar:
                        self.texto_voz(answer, voz_id=None)

if __name__ == '__main__':
    aurora = AuRoRa()
    aurora.main()

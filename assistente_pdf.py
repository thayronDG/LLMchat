import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3 or (elevenlabs)
import ollama
import os
import pandas as pd
import pdfplumber
from llama_index.core import SimpleDirectoryReader
from llama_parse import LlamaParse
from llama_index.readers.file import (

    PDFReader,
    HTMLTagReader,
    ImageReader,
    PyMuPDFReader,
    XMLReader,
)

class AuRoRa():
    def __init__(self, path):
        self.mensagens = [{"role": "system", "content": "Você é uma assistente virtual para aplicações de inteligência artificial e seu nome é AuRoRa. Vou te passar a extração de textos de faturas de conta de luz, e seu objetivo é organizar o texto extraido. Pode haver tabelas, código de barras e várias informações. Quero que você extraia e organize TODAS que exstirem tanto de consumo e valores e datas quanto de pagamento. NÃO QUERO RESUMIDO. Ex: Consumo não compensado 100Kwh Valor R$100,00. Pode ser que o texto extraido não esteja perfeito, mas quero que você faça o melhor possível. Se precisar de mais informações, me avise. Vamos começar?"}]
        self.sem_palavra_ativadora = True
        self.entrada_por_pdf = True
        self.image = False
        self.path = path
        
        # ollama.api_key = os.getenv('OLLAMA_API_KEY') 

    def chatbot(self, messages):
        """
        A function that interacts with the Ollama chatbot to generate a response based on the given messages.
        """
        # for part in ollama.chat(model='llama3.1', messages=messages, stream=True):
        #     print(part['message']['content'], end='', flush=True)
            
        response = ollama.chat('llama3.1', messages=messages)
        return response['message']['content']


    def bot2pdf(self):
        """
        Converts the given text to speech using the specified voice ID.
        """

        # Criar parser do LlamaParse com formato Markdown (mantém tabelas)
        parser = LlamaParse(api_key="llx-azC46TwldP3Qnw1Sszsq1F36KxLncE1UFPIvSfbxsEIySX1O", output_format="markdown")
        # Ler o PDF
        documents = parser.load_data("10034246680.pdf")
        # print(documents)
        
        # parser = PDFReader()
        # file_extractor = {".pdf": parser}
        # documents = SimpleDirectoryReader(
        #     self.path, file_extractor=file_extractor
        # ).load_data()
        
        return documents
        

    def bot2image(self):
        """
        Função responsável por capturar áudio do microfone e realizar o reconhecimento de fala.
        """
        parser = ImageReader()
        file_extractor = {
            ".jpg": parser,
            ".jpeg": parser,
            ".png": parser,
        }  # Add other image formats as needed
        documents = SimpleDirectoryReader(
            self.path, file_extractor=file_extractor
        ).load_data()
        return documents

    def main(self):
        """
        This function represents the main entry point of the program.
        It interacts with the user by asking questions and providing answers using a chatbot.
        """
        print("AuRoRa iniciada...\n")
        
        while True:
            question = ""
            
            if self.entrada_por_pdf:
                question = self.bot2pdf()
            elif self.image:
                question = self.bot2image()

            self.mensagens.append({"role": "user", "content": str(question)})
            answer = self.chatbot(self.mensagens)
            self.mensagens.append({"role": "assistant", "content": answer})
            print("\n-> AuRoRa:", answer)
            print()


if __name__ == '__main__':
    aurora = AuRoRa(path="input")
    aurora.main()


import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3 
import pandas as pd
import streamlit as st
from class_aurora import AuRoRa

assistente = AuRoRa()

def main():
    with st.sidebar:
        name = st.text_input("Your Name")
        st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
        st.markdown("[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)")
        st.markdown("[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)")
    
    st.title('💬 AuRoRa - Assistente Virtual')
    st.caption("🚀 A Streamlit chatbot powered by Llama")
    st.write('Olá! Eu sou a AuRoRa, uma assistente virtual para aplicações de inteligência artificial. Como posso te ajudar?')

    # Initialize messages if not already present
    if 'messages' not in st.session_state or 'user_name' not in st.session_state:
        st.session_state['messages'] = [{"role": "system",
                                         "content": f"Você é uma assistente virtual para aplicações de inteligência artificial e seu nome é AuRoRa. E meu nome é {name if name else '"usuário"'}"}]
        st.session_state['user_name'] = name if name else 'usuário'
    
    # Update user name and system message if name changes
    if name and st.session_state['user_name'] != name:
        st.session_state['user_name'] = name
        st.session_state['messages'][0]['content'] = f"Você é uma assistente virtual para aplicações de inteligência artificial e seu nome é AuRoRa. E meu nome é {name}"
    
    # Display messages
    for msg in st.session_state['messages']:
        st.chat_message(msg["role"]).write(msg["content"])
    
    # Handle user input and generate response
    if prompt := st.chat_input():
        if not name:
            st.info("Please add your name to continue.")
            st.stop()
        st.session_state['messages'].append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = assistente.chatbot(st.session_state['messages'])
        st.session_state['messages'].append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

if __name__ == '__main__':
    main()


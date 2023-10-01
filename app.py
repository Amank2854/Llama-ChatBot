import streamlit as st
import os
from ctransformers import AutoModelForCausalLM
from langchain.llms import CTransformers

# App title
st.set_page_config(page_title="Llama 2 Gita Chatbot 🦙💬",
                   page_icon="🦙",
                   layout = "centered",
                   initial_sidebar_state="collapsed")


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

@st.cache_resource()
def ChatModel(temperature, top_p):
    return AutoModelForCausalLM.from_pretrained(
        'llama-2-7b-chat.ggmlv3.q2_K.bin', 
        model_type='llama',
        temperature=temperature, 
        top_p = top_p)


with st.sidebar:
    st.title('Llama 2 Gita Chatbot 🦙💬')
    

    
    temperature = 0.5
    top_p = 0.5

    chat_model =ChatModel(temperature, top_p)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome to Gita ChatBot, How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome to Gita ChatBot, How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as Assistant quoting examples from The Bhagavad Gita with verse and chapter numbers and in 50 words. Give only one response as a assistant, do not continue the conversation, just one response as assistant.\n"
   
    # add last two messages to string_dialogue
    for dict_message in st.session_state.messages[max(-3,-len(st.session_state.messages)):]:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"

    print(f"prompt {string_dialogue} Assistant: ")
    output = chat_model(f"prompt {string_dialogue} Assistant: ")
    return output

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# Streamlit UI
st.title("VC Show Chat Bot")
input_txt = st.text_input("Please enter your queries here...")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is Volunteer Connect."),
    ("user", "User query: {query}")
])

# LLM setup
llm = Ollama(model="llama2")

# Output parser
output_parser = StrOutputParser()

# Chain definition
chain = prompt | llm | output_parser

# Run the chain if there's input
if input_txt:
    response = chain.invoke({"query": input_txt})
    st.write(response)

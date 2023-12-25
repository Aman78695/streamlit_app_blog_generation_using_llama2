import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLlamaresponse(input_text,no_words,style):
    llm=CTransformers(model='llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama')
    
    prompt="""write a blog for {style} on the topic {input_text} in {no_words} words"""

    response=llm(prompt)
    return response


st.set_page_config(page_title='Generate_Blog',
                   page_icon='👋🏻',
                   layout='centered')

st.header('Generate Blogs')

input_text=st.text_input('Write the topic of blog')

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('input the no of words')

with col2:
    style=st.selectbox('choose the type',('research','data science','common people'))

submit=st.button('Generate')

if submit:
    st.write(getLlamaresponse(input_text,no_words,style))
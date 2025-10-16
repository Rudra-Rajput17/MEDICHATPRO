import streamlit as st

def pdf_uploader():
    return st.file_uploader("Upload a pdf file" , type =["pdf"],accept_multiple_files = True , help = "upload one or more file to proccess")

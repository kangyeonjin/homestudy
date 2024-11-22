import streamlit as st
import requests

st.title("Streamlit with FastAPI and Pinecone")

# Example call to FastAPI
response = requests.get("http://fastapi:8000/")
if response.status_code == 200:
    st.write(response.json())
else:
    st.write("FastAPI is not responding.")

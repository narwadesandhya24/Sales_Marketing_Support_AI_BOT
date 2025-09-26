import streamlit as st
import requests

BACKEND = "http://localhost:8000"  # <== CHANGE IF DEPLOYED REMOTELY

st.title("Sales, Marketing & Support Agent")

mode = st.sidebar.selectbox("Choose Module", ["Support", "Recommender", "Social Media"])

if mode == "Support":
    q = st.text_input("Ask a question")
    if st.button("Ask") and q:
        r = requests.post(BACKEND + "/support", json={"text": q}).json()
        st.write(r)

elif mode == "Recommender":
    q = st.text_input("Describe your need")
    if st.button("Recommend") and q:
        r = requests.post(BACKEND + "/recommend", json={"text": q}).json()
        st.write(r)

else:
    q = st.text_input("Topic for content")
    if st.button("Generate") and q:
        r = requests.post(BACKEND + "/social", json={"text": q}).json()
        st.write(r)

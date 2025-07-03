import streamlit as st
st.title("JOIN AN INTERACTIVE LIVE CLASS WITH CHEF RISHI!")
st.write("bake ur information below")
name=st.text_input("Enter your name:")
if st.button("submit:)"):
   st.write(f" Nice to meet u ,{name},lets join an experience to bake a cake!.")

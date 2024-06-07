import streamlit as st

st.markdown("# Extraescolar Bananas 🐒")

if st.button("Matrícula"):
    st.switch_page("pages/2-Matricula.py")
if st.button("Horarios"):
    st.switch_page("pages/3-Horarios.py")
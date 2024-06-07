import streamlit as st
import pandas as pd
import numpy as np

if st.button("Home"):
    st.switch_page("pages/1-Home.py")
if st.button("Matrícula"):
    st.switch_page("pages/2-Matricula.py")
if st.button("Horarios"):
    st.switch_page("pages/3-Horarios.py")
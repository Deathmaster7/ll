import streamlit as st
import base64
from sphoto import show

columns = st.columns((2, 1, 2))
button_pressed = columns[1].button('CLICK HERE')

if button_pressed:
    show()




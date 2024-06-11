import streamlit as st
import base64


def show():
    st.markdown("""
    <style>
    .big-font {
        font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .loda-font {
        font-size:40px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .heart-font {
        font-size:80px !important;
    }
    </style>
    """, unsafe_allow_html=True)





    st.image('lp.jpeg')
    st.markdown("----", unsafe_allow_html=True)
    st.markdown('<p class="big-font">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First of Many Adventures Together 💩</p>', unsafe_allow_html=True)
    st.markdown('<p class="loda-font">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Two Hearts, One Soul !! </p>', unsafe_allow_html=True)
    st.markdown('<p class="heart-font">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;♡♡</p>', unsafe_allow_html=True)


    st.markdown("----", unsafe_allow_html=True)



    st.audio("local_audio.mp3", autoplay=True)
    st.markdown("----", unsafe_allow_html=True)

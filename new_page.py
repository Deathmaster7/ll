import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:35px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Happy Birthday, Ruhin!</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">From the moment I met you, my life has been filled with joy, love, and endless happiness. You are my </p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">sunshine, my rock, and my best friend. I am so grateful for every moment we share, every smile we</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">exchange, and every laugh we enjoy together.</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">On this special day, I want to remind you how incredibly special you are to me. Your kindness,</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">beauty, and strength inspire me every day. Thank you for being you, and for letting me be a part of </p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">your amazing life.</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">May your birthday be as wonderful and extraordinary as you are. Here’s to many more memories, </p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">adventures, and celebrations together.</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">I love you more than words can express. Happy Birthday, my love!</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">With all my heart,</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">Aryaman</p>', unsafe_allow_html=True)
url='google.com'
# Custom CSS to inject
st.markdown("""
<style>
button{
    height: 75px; /* Adjust the height as needed */
    font-size:24px;
    width:250px;
    border-radius: 25px; /* Optional: for rounded buttons */
    padding: 17px 40px 25px 40px;
    

}
</style>
""", unsafe_allow_html=True)

st.markdown("----", unsafe_allow_html=True)
columns = st.columns((2, 1, 2))
button_pressed = columns[1].markdown(f'''
<a href={url}><button>Press Again ♡</button></a>
''',
unsafe_allow_html=True)
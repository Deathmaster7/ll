import streamlit as st


url = 'https://youare.streamlit.app/'
st.markdown("""
    <style>
        .stApp {
        background: url("https://i.imgur.com/GQpxlOj.jpeg");
        background-size: cover;
        }
    </style>""", unsafe_allow_html=True)


original_title = '<p style="font-family:Ariel; color:#D90166; font-size: 105px;">HAPPY &nbsp;&nbspBIRTHDAY &nbsp;&nbsp;&nbsp;&nbsp;&nbspBABY GIRL</p>'
st.markdown(original_title, unsafe_allow_html=True)

st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)

# Custom CSS to inject
st.markdown("""
<style>
button{
    height: 80px; /* Adjust the height as needed */
    font-size:24px;
    width:159px;
    border-radius: 25px; /* Optional: for rounded buttons */
    padding: 17px 40px 35px 40px;
    

}
</style>
""", unsafe_allow_html=True)

st.markdown("----", unsafe_allow_html=True)
columns = st.columns((2, 1, 2))
button_pressed = columns[1].markdown(f'''
<a href={url}><button>Press ♡</button></a>
''',
unsafe_allow_html=True)
st.markdown("----", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)



st.image('heart.jpg')

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Tiny5&display=swap" rel="stylesheet');

			html, body, [class*="css"]  {
			font-family: 'Tiny5', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)


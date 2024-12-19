import streamlit as st
import streamlit.components.v1 as components

# Load the HTML content
with open("ping_pong.html", "r") as file:
    html_content = file.read()

# Define the Streamlit app
st.set_page_config(
    page_title="Ping Pong Game",
    layout="wide",
)

st.title("Ping Pong Game")
st.markdown(
    "Play the game below. It adjusts to the size of your browser window. Enjoy!"
)

# Embed the HTML
components.html(
    html_content,
    height=st.session_state.get("browser_height", 800),  # Default height
    scrolling=False,
)

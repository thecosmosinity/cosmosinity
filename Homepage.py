import streamlit as st

st.set_page_config(page_title="Hompage", page_icon=":wave", layout="wide")
st.sidebar.success("Select A Page!")


st.title("Homepage")
st.subheader("This is the first page you will see! See that sidebar, Select any page from there!")

# Use Local CSS code
def css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
css("style/style.css")

st.write("© 2024 - 2024 cosmosinity - All Rights Reserved.")
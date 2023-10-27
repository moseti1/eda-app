import streamlit as st

st.text('Hello World')
orig_title = '<p style="font-family:Courier; color:Blue; font-size:20px;"> Hello World </p>'
st.markdown(orig_title, unsafe_allow_html=True)

new_title = '<p style="font-family:sans-serif; color:Green; font-size:42px;"> Hello World </p>'
st.markdown(new_title, unsafe_allow_html=True)

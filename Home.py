import streamlit as st


st.set_page_config(page_title='Attendance System',layout='wide')
st.header('Attendance System Using Face Recoginition')

with st.spinner("Loading Models & Connecting to Redis Database"):
    import Face_rec

st.success("Models loaded succesfully")
st.success("Redis Database succesfully connected")
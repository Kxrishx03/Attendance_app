import streamlit as st
from Home import Face_rec

#st.set_page_config(page_title='Report')
st.subheader('Reporting')

#Retrive & show logs data

## Extract data from redis list

name = 'attendace:logs'

def load_los(name):
    logs_list = Face_rec.r.lrange(name,start=0,end=-1)
    return logs_list

## Create tabs to show info

tab1,tab2 =st.tabs(['Registered Users','Logs'])

with tab1:
    if st.button('Refresh Data'):
        with st.spinner("Retriving data from Database"):
            redis_face_db = Face_rec.retrive_data(name='academy:register')
            st.dataframe(redis_face_db[['Name','Role']])


with tab2:
    if st.button('Refresh Logs'):
        st.write(load_los(name=name))



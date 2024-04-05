import streamlit as st
import numpy as np
from streamlit_webrtc import webrtc_streamer
import av
from Home import Face_rec

#st.set_page_config(page_title='Registration Form')
st.subheader('Registration Form')

## Initialize registrtion form
registration_form = Face_rec.RegistrationForm()

## Step 1 :Collect person name & role
## Form
person_name = st.text_input(label="Name",placeholder="Full Name")
role = st.selectbox(label="Select your role",options=('Student','Teacher'),placeholder="Select Role")

## Step 2 : Collect Facial embeddings of the person

def video_callback_fun(frame):
    img = frame.to_ndarray(format='bgr24')
    reg_img,embedding = registration_form.get_embeddings(img)
    ## Two step process
    ## Save data in local computer
    if embedding is not None:
        with open('face_embedding.txt',mode ='ab') as f:
            np.savetxt(f,embedding)

    return av.VideoFrame.from_ndarray(reg_img,format='bgr24')

webrtc_streamer(key='registration',video_frame_callback=video_callback_fun)


## Step 3: Save the data in redis database

if st.button('Submit'):
    return_val = registration_form.save_data_in_redis_db(person_name,role)
    if return_val == True:
        st.success(f"{person_name} Registered successfully")
    elif return_val == 'name_false':
        st.error('Plese enter the name: Name cannot be empty or spaces')
    elif return_val == 'file_false':
        st.error('face_embedding.txt is not found.Please try again after refresh!') 
           

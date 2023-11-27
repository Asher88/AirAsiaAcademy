import streamlit as st
import pandas as pd
import pickle

st.write("""
#Advertising Platform

This app predicts sales base on budget You Put On **TV**,**Radio**,**Newspaper**
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 1.0, 300, 100)
    Radio = st.sidebar.slider('Radio', 1.0, 300, 10)
    Newspaper = st.sidebar.slider('Newspaper', 1.0, 300, 10)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("AdvertisementModul.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)

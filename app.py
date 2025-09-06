# To run this app, use the command: streamlit run app.py

import streamlit as st
import numpy as np
import joblib
model=joblib.load('crop_recommendation_model.pkl')
model



#create title crop recommendation
st.title("Crop Recommendation System")
st.write("This app recommends the best crop to grow based on N,P,K and weather conditions.")
#set numerical input
a = st.number_input("Nitrogen")
b = st.number_input("Phosphorus")
c = st.number_input("potassium")
d = st.number_input("temperature")
e = st.number_input("humidity")
f= st.number_input("ph")
g= st.number_input("rainfall")

btn=st.button("Predict")    
if btn:
    input=np.array([[a,b,c,d,e,f,g]])
    prediction=model.predict(input)
    print(prediction)

    st.subheader(prediction[0])
st.write("Built by Rajan Lamichhane")

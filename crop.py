import streamlit as st
import pandas as pd
import pickle
import numpy as np


#from PIL import Image
model = pickle.load(open('C:/Users/Rupeshwar/.spyder-py3/apps/Resources/RandomForest.sav', 'rb'))


def app():

    st.title("Crop Prediction")
    
            
    st.subheader("Enter the data for the following inputs")
    
    N = st.number_input("Nitrogen Value : ")
    P= st.number_input("Phosphorus value : ")
    K= st.number_input("Potassium Value : ")
    temp = st.number_input("Temperature: ")
    humidity = st.number_input("Humidity : ")
    pH = st.number_input("pH value: ")
    rainfall = st.number_input("Rainfall : ")
    #print(type(N))
    
    diag=' '
    
    if st.button("Predict Crop"):
        diag=predict([N,P,K,temp,humidity,pH, rainfall])
        #st.success(diag)
        result= ' '.join(map(str, diag))
        result1= result.upper()
        
        st.success('The most suitable crop for your field is {}'.format(result))
        st.success(result1)
    
    
def predict(input_d):
    input_d = np.asarray(input_d)
    input_re = input_d.reshape(1,-1)
    prediction = model.predict(input_re)
    print(prediction)
    
    if(prediction is not None):
        #st.header(prediction)
        return(prediction)
    else:
        return "None"
    
    
    
    
    
#streamlit run C:/Users/Rupeshwar/.spyder-py3/app.py
#https://www.kaggle.com/code/mnavaidd/casava-leaf-disease-classification-with-keras
    

    
    

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly

#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def app():
    st.title("General Quiz about the Crop")
    crop = st.radio("Which Crop do you know the most about?",
     ('Wheat', 'Rice', 'Cotton'))

    if crop == 'Wheat':
     st.write('You selected Wheat.')
     
     Color=st.selectbox('Color', ['Red','White','Golden','Brown'])
     Rainfall=st.selectbox('Select Rainfall', ('50cm to 100cm','Above 200cm','Less Than 30 cm'))
     Temperature=st.selectbox('Select Temperature', ('20 C-25 C ','Above 40 C','55 C- 60C'))
     Soil=st.selectbox('Select Soil Type', ['Clay Loam','Black','Red','Loamy'])
     pH=st.selectbox('Select pH', ('6-7','Above 8','1'))
     
     submit = st.checkbox('Submit')
     if submit:
         if Color =='Golden' and Rainfall =='50cm to 100cm' and Temperature == '20 C-25 C ' and Soil=='Clay Loam' and pH=='6-7':
             st.success('You are 100% right!!!')
         else:
             st.warning('missing Something, check Again!!!')
     
     
         
    elif crop =='Rice':
        st.write("You  selected Rice.")
                
        Color=st.selectbox('Color', ['Green','White','Golden','Brown'])
        Rainfall=st.selectbox('Select Rainfall', ['50cm to 100cm','Above 200cm','Less Than 100 cm','100cm'])
        Temperature=st.selectbox('Select Temperature', ('20 C-25 C ','Above 20 C','21 C- 40 C'))
        Soil=st.selectbox('Select Soil Type', ['Clay Loam','Black','Red','Clay'])
        pH=st.selectbox('Select pH', ('2','Above 9','6'))
        
        submit = st.checkbox('Submit')
        if submit:
            if Color =='White' and Rainfall =='100cm' and Temperature == '20 C-41 C ' or Soil=='Clay Loam' and Soil == 'Clay' and pH=='6':
                st.success('You are 100% right!!!')
            else:
                st.warning('missing Something, check Again!!!')
                
    elif crop == 'Cotton':
        st.write("You  selected Cotton.")
                
        Color=st.selectbox('Color', ('Brown','White','Golden'))
        Rainfall=st.selectbox('Select Rainfall', ('50cm','Above 100 cm','50 cm -75 cm'))
        Temperature=st.selectbox('Select Temperature', ('20 C-25 C ','Less then 30 C','20 C- 32C'))
        Soil=st.selectbpx('Select Soil Type', ['Alluvial','Clay','Loamy','Black'])
        pH=st.selectbox('Select pH', ['6-7','Above 8','4-6.5','6-6.5'])
        submit = st.checkbox('Submit')
        
        if submit:
            if Color =='Golden' and Rainfall =='50cm to 100cm' and Temperature == '20 C-25 C ' and Soil=='Black' or  Soil=='Alluvial' and pH=='6-7':
                st.success('You are 100% right!!!')
            else:
                st.warning('missing Something, check Again!!!')
    


#streamlit run C:/Users/Rupeshwar/.spyder-py3/app.py
    
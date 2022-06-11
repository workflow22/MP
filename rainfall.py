import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px
#from PIL import Image




def app():
    
    st.title("Rainfall Analysis")
    
    #data = st.file_uploader("Upload the csv", type=["csv"])
    #df=pd.read_csv(data)
    #if data is not None:
        ##st.write(type(data))
        #st.dataframe(df)
    df= pd.read_csv(r'C:/Users/Rupeshwar/.spyder-py3/apps/Resources/rainfall.csv')
    col4, col5, col6 = st.columns(3)
    with col5: 
        st.subheader('Chart displaying Rainfall of 10 Years')
        fig = px.pie(df,values='ANNUAL', names='Region',title='Rainfall Data')
        st.write(fig)
   
    
    st.subheader('Chart displaying Rainfall for the Year')
    fig= df[['YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL','AUG', 'SEP', 'OCT', 'NOV', 'DEC']].groupby("YEAR").sum()
    st.line_chart(fig)


    st.subheader('Bar Chart displaying Rainfall for the Year')
    fig4=df[['YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
       'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].groupby("YEAR").sum()
    st.bar_chart(fig4)


    
    #streamlit run C:/Users/Rupeshwar/.spyder-py3/app.py
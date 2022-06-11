import streamlit as st
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly_express as px

def app():

    st.title("Statistics of the Crop Sale")

    data = st.file_uploader("Upload the csv", type=["csv"])
    if data is not None:
        st.write(type(data))
        df=pd.read_csv(data)
        st.dataframe(df)
        
    col4, col5 = st.columns(2)
    
    with col4:
        st.subheader('Pie Chart displaying  of Crops Income for the year')
        fig3 = px.pie(df,values='Income', names='Crop')
        st.write(fig3)
        
    with col5:
        st.subheader('Pie Chart displaying  of Crops Investement for the year')
        fig2 = px.pie(df,values='Invested', names='Crop')
        st.write(fig2)
        
    col8, col9= st.columns(2)
    
    with col8:
        st.subheader('Pie Chart displaying Statistics of Farmers Crop Transportation')
        fig4 = px.pie(df,values='Transport', names='Crop')
        st.write(fig4)
    with col9:
        st.subheader('Pie Chart displaying Quantity of the Crops grown')
        fig = px.pie(df,values='Quantity', names='Crop')
        st.write(fig)
    
    col6, col7 = st.columns(2)
    
    with col6:
        st.subheader('Chart displaying Income of Farmers Crop Sale')
        bar_chart= alt.Chart(df).mark_bar().encode(
        y='Income',
        x='Crop')
        st.altair_chart(bar_chart,use_container_width=True)
    with col7:
        st.subheader('Chart displaying Quantity of Crops grown ')
        bar_chart1= alt.Chart(df).mark_bar().encode(
        y='Quantity',
        x='Crop')
        st.altair_chart(bar_chart1,use_container_width=True)


    
    
#streamlit run C:/Users/Rupeshwar/.spyder-py3/app.py
    
    
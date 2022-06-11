import streamlit as st
import pandas as pd
import folium
from PIL import Image

from streamlit_folium import folium_static  


def app():
    
    
    st.subheader("Cultivation rate of Indian States")
    #data = st.file_uploader("Upload the csv", type=["csv"])
    #add=pd.read_csv(data)
    #if data is not None:
     #   st.write(type(data))
        
    add= pd.read_csv(r'C:/Users/Rupeshwar/.spyder-py3/apps/Resources/Map.csv')
        

    co1, col2, col3 = st.columns(3)
    co4, col5, col6= st.columns(3)
    

    with col2:
        st.write('Map displaying the Irrigated Land in India')
        all_add = folium.Map(zoom_start=4,location=[20.5937, 78.96])
        
        for _, address in add.iterrows():
            folium.Marker(
                location=[address['Latitude'], address['Longitude']],
                popup=address['PInfo'],
                tooltip=address['State']).add_to(all_add)
        folium_static(all_add)
    
    with col5:
        all_adds = folium.Map(zoom_start=5,location=[20.5937, 78.96])
        
        st.write('Map displaying the UnIrrigated Land in India')
        for _, address in add.iterrows():
            folium.Marker(
                location=[address['Latitude'], address['Longitude']],
                popup=address['NInfo'],
                tooltip=address['State']).add_to(all_adds)
        folium_static(all_adds)

   


                
                
                
                
#streamlit run C:/Users/Rupeshwar/.spyder-py3/app.py
	

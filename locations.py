import streamlit as st
import folium
import pandas as pd
from PIL import Image
from streamlit_folium import folium_static
def app():


    st.subheader("Lets find the nearest Crop Help Center")
    
    # = st.file_uploader("Upload the csv", type=["csv"])
    #add=pd.read_csv(data)
    #if data is not None:
        #st.write(type(data))
    add= pd.read_csv(r'C:/Users/Rupeshwar/.spyder-py3/apps/Resources/add2.csv')
        

    
    all_add = folium.Map(zoom_start=5,location=[20.5937, 78.96])
    

    for _, address in add.iterrows():
        folium.Marker(
            location=[address['Latitude'], address['Longitude']],
            popup=address['Location'],
            tooltip=address['Agricultural Research Center']).add_to(all_add)
    folium_static(all_add)
  
    option = st.sidebar.selectbox('State',('Andhra Pradesh','Bhopal','Chennai','Haryana','Hyderabad', 'Kerala','Maharashtra', 'Mysore',
                                          'New Delhi','Odisha','Rajasthan','Tamil Nadu','Uttar Pradesh','West Bengal'))
    st.write('You selected:', option)
    if option == "Andhra Pradesh":
        st.header("National Academy of Agricultural Research Management")
        st.subheader("ICAR, NAARM Campus, Rajendranagar mandal, Hyderabad, Telangana 500030")
        st.subheader("Phone Number: 040 2458 1300")
        
    
    elif option == "Bhopal":
        st.header("Central Institute of Agricultural Engineering")
        st.subheader(" Berasia Rd, Navi Bagh, Bhopal, Madhya Pradesh 462038")
        st.subheader("Phone Number: 0755 273 7191")
       
        
        
    elif option == "Chennai":
        st.header("Central Institute of Brackishwater Acquaculture")
        st.subheader("MRC Nagar, Raja Annamalai Puram, Chennai, Tamil Nadu 600028") 
        st.subheader("Phone Number: 044 2461 8817")
        
        
        
    elif option == "Haryana":
        st.header("Directorate of Wheat Research	")
        st.subheader("DWR RdGahoon Vihar, Karnal, Haryana 132001")
        st.subheader("Phone Number: 040 2458 1300")
                
        st.header("National Dairy Research Institute")
        st.subheader(" GT Rd, near Jewels Hotel, Nyaypuri, Karnal, Haryana 132001")
        
       
    elif option == "Hyderabad":
        st.header("National Institute of Agricultural Extension Management")
        st.subheader("Manage Rd, Police Quaters, Rajendranagar mandal, Hyderabad, Telangana 500030")
        st.subheader("Phone Number: 040 2401 6702")
        
        
    elif option == "Kerala":
        st.header("Central Plantation Crops Research Institute")
        st.subheader("Chowki, Kerala 671124")
        st.subheader("Phone Number: 04994 232 894")

    elif option == "Maharashtra":
        st.header("Central Institute for Cotton Research")
        st.subheader("Panjari, Wardha Rd, Nagpur, Maharashtra 441108")
        st.subheader("Phone Number:  098505 63000")

        
    elif option == "Mysore":
        st.header("Central Food Technological Research Institute")
        st.subheader("Cheluvamba Mansion, Valmiki Main Rd, opp. Railway Museum, Devaraja Mohalla, CFTRI Campus, Kajjihundi, Mysuru, Karnataka 570020")
        st.subheader("Phone Number: 040 2458 1300")

        
        
    elif option == "New Delhi":
        st.header("Indian Agricultural Research Institute	")
        st.subheader("ICAR-Indian Agricultural Research Institute, Pusa Campus,New Delhi - 110012")


        
    elif option == "Odisha":
        st.header("Central Institute of Freshwater Aquaculture")
        st.subheader("ICAR-Central Institute of Freshwater Aquaculture, Kausalyaganga, Bhubaneswar-751002, ODISHA, INDIA")
        st.subheader("Phone Number: 040 2458 1300")

        
        
    elif option == "Rajasthan":
        st.header("Central Arid Zone Research Institute")
        st.subheader("Cazri Rd, near Industrial Training Institute, Jodhpur, Rajasthan 342003")
        st.subheader("Phone Number: 0291 278 6584")
        
        st.header("National Institute of Agricultural Marketing")
        st.subheader("Kota Rd, Sanganer, Bambala, Jaipur, Rajasthan 302033")
        st.subheader("Phone Number: 0141 277 0027")

        
        
    elif option == "Tamil Nadu":
        st.header("Sugarcane Breeding Institute	")
        st.subheader("Sugar Cane Institute Rd, Near Behind, Tamil Nadu Agricultural University, Karumalai Chettipalayam, Veerakeralam, Tamil Nadu 641007")
        st.subheader("Phone Number: 0422 247 2621")

        
        
    elif option == "Uttar Pradesh":
        st.header(" National Botanical Research Institute")
        st.subheader("Rana Pratap Marg, Prem Nagar, Hazratganj, Lucknow, Uttar Pradesh 226001")
        st.subheader("Phone Number: 0522 229 7802")
        
        st.header("Central Institute for Research on Goats")
        st.subheader("Farah Main Bazar Rd, Makhdum, Uttar Pradesh 281122")

    elif option == "West Bengal":
        st.header("Central Inland Fisheries Research Institute	")
        st.subheader(" Barrackpore, Monirampore, Kolkata, West Bengal 700120")
        st.subheader("Phone Number: 033 2592 0177")

        
    else:
        st.subheader("None found")
        
        
#streamlit run C:/Users/Rupeshwar/.spyder-py3/app.py
    
    
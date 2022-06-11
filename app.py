import streamlit as st
from multiapp import MultiApp
from app import home,  crop, locations, rainfall , db, new, price

from PIL import Image
st.set_page_config(layout="wide")


app = MultiApp()
st.title("AGRODEC WEBSITE")
img1 = Image.open(r"C:\Users\Rupeshwar\.spyder-py3\apps\Resources\logo.png")
img1 = img1.resize((400,200))
st.image(img1,use_column_width="False")

# Title of the main page


# Add all your applications (pages) here
app.add_app("Home Page", home.app)
app.add_app("Crop Prediction", crop.app)
app.add_app("Statistics", db.app)
app.add_app("Research Centers", locations.app)
app.add_app("Rainfall", rainfall.app)
app.add_app("Quiz", new.app)
app.add_app("Information Portal", price.app)


# The main app
app.run()







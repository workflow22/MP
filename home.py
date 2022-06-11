import streamlit as st
from PIL import Image



def app():

    st.title("Welcome to AGRODEC!!!!")
    st.subheader("Meet the Team")
    
    col1, col2 , col3 = st.columns(3)
    
    with col1:
        img2 = Image.open(r"C:\Users\Rupeshwar\.spyder-py3\apps\Resources\Rupesh.jpg")
        img2 = img2.resize((280,280))
        st.image(img2,use_column_width="False")
        
    with col2:
        img4 = Image.open(r"C:\Users\Rupeshwar\.spyder-py3\apps\Resources\Riya.jpeg")
        img4 = img4.resize((280,280))
        st.image(img4,use_column_width="False")
        
        

    with col3:
        img3 = Image.open(r"C:\Users\Rupeshwar\.spyder-py3\apps\Resources\Priyanka.jpg")
        img3 = img3.resize((280,280))
        st.image(img3,use_column_width="False")
        
    col4, col5, col6 = st.columns(3)
        
    
    with col4:
        st.markdown("""## Name: Rupeshwar.Rao""",True)
        st.markdown("""### Roll No: 2183179""",True)
        st.markdown("""### Role: Project Developer Lead""", True)
        st.markdown("""### Class: CORE""", True)
      
        
    with col5:
        st.markdown("""## Name: Riya. Goyal""",True)
        st.markdown("""### Roll No: 2183173""",True)
        st.markdown("""### Role:Project Developer""", True)
        st.markdown("""### Class: Intelligent Systems""", True)
      
    with col6:
        st.markdown("""## Name: Priyanka. Jha""",True)
        st.markdown("""### Roll No: 2183168""",True)
        st.markdown("""### Role: Project Developer""", True)
        st.markdown("""### Class: Intelligent Systems""", True)
        
        
    
    
    







#streamlit run C:/Users/Rupeshwar/.spyder-py3/app.py
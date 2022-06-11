import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import sklearn as sk




#from PIL import Image
model = pickle.load(open('C:/Users/Rupeshwar/.spyder-py3/apps/Resources/RandomForest.sav', 'rb'))

input_d=(90,42,43,21,80,7,203)
input_d = np.asarray(input_d)
input_re = input_d.reshape(1,-1)
prediction = model.predict(input_re)
print(prediction)
    
if(prediction is not None):
    print("The crop which can be produced is: "+prediction)
else:
    print("None")
    



    
    
#streamlit run C:/Users/Rupeshwar/.spyder-py3/app.py
    

    
    

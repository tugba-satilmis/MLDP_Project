import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

import pandas as pd
import numpy as np


# st.title("Car Price Prediction")
# st.header('This is a header')
# st.subheader('Car Price Prediction')
# st.text('This is some text.')
# st.write('Hello, *World!* :sunglasses:')
st.markdown("<h2 style='text-align:center; color:floralWhite;'>Car Price Prediction</h2>", unsafe_allow_html=True)

# st.success('This is a success message!')
# st.info('This is a purely informational message')
# st.error('This is an error')

# st.help(range)

col1, col2, col3 = st.columns([1,8,1]) 

#Image
try:
    # Some Code
    #read local image
    from PIL import Image
#     img1 = Image.open("images.jpeg")

    #image url
    url = "https://d3ftmvynp162pm.cloudfront.net/public/album_photo/73/5c/05/6b6e5f35f357d06c9f8decf2210d2dd0.jpg"

    with col2:
        st.image(url, caption="Predicting the Prices of Cars")
    
except:
    # Executed if error in the
    # try block
    st.text("Image Not Read.")
    
else:
    # execute if no exception
    pass
          
finally:
    # Some code .....(always executed)   
    pass


# read Dataset
df = pd.read_csv("final_scout.csv")

with col2:
    if st.checkbox("Show dataframe"):
        st.write(df)
   

# Creating side bar 
st.sidebar.subheader("Select the features you want for price estimation")

input_make_model = st.sidebar.radio("Name of the Car Model:", df["make_model"].unique())

input_Gearing_Type = st.sidebar.radio("Name of the Car Model:", df["Gearing_Type"].unique())

input_hp_kW  = st.slider("Horse Power(kW)", df["hp_kW"].min(), df["hp_kW"].max(), float(df["hp_kW"].mode()[0]), 1.0)

input_km = st.sidebar.slider("Kilometre(km)", 0.0 ,df["km"].max(), float(df["km"].mode()[0]), 1.0)

input_age = st.sidebar.slider("Car Age", 0.0 , df["age"].max(), float(df["age"].mmode()[0]), 1.0)

input_gears = st.sidebar.slider("Gears", df["Gears"].min() , df["Gears"].max(), float(df["Gears"].mode()[0]), 1.0)

import pickle
model = pickle.load(open("final_model_scout", "rb"))

data =  {"make_model" : input_make_model,
        "Gearing_Type" : input_Gearing_Type,
        "age" : input_age,
        "hp_kW" : input_hp_kW,
        "km" : input_km ,
        "Gears" : input_gears}
input_data = pd.DataFrame(data, index=[0])


# button to see dataset
if st.button("Make Prediction"):
    prediction = model.predict(input_data)[0].round(2)
    st.success(f'Analyze Predict:&emsp;{prediction}')
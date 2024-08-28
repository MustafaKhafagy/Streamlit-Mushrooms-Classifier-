
import streamlit as st
import joblib
import pandas as pd

inputs = joblib.load("columns_name.pkl")

pipeline = joblib.load("pipleline.pkl")

st.header("Mushroms Classifier  ")

col1 , col2 = st.columns(2)
with col1 :
    st.header("Is it POISONOUS ?")
    st.image("attachment-mushroom-feature-1.jpg")
with col2 :
    st.header("Is it EDIBLE ?") 
    st.image("_WP__fall-mushroom-puffball-1920x1435.jpeg")

def prediction(cap_diameter, cap_shape, cap_surface, cap_color,oes_bruise_or_bleed, gill_attachment, gill_spacing, gill_color,
                stem_height, stem_width, stem_root, stem_surface, stem_color,
                veil_color, has_ring, ring_type, spore_print_color, habitat,season):
    df = pd.DataFrame(columns=['cap_diameter', 'cap_shape', 'cap_surface', 'cap_color',
       'does_bruise_or_bleed', 'gill_attachment', 'gill_spacing', 'gill_color',
       'stem_height', 'stem_width', 'stem_root', 'stem_surface', 'stem_color',
       'veil_color', 'has_ring', 'ring_type', 'spore_print_color', 'habitat',
       'season'])
    df.at[0, "cap_diameter"] = cap_diameter
    df.at[0, "cap_shape"] = cap_shape
    df.at[0, "cap_surface"] = cap_surface
    df.at[0, "cap_color"] = cap_color
    df.at[0, "does_bruise_or_bleed"] = does_bruise_or_bleed
    df.at[0, "gill_attachment"] =gill_attachment
    df.at[0, "gill_spacing"] =gill_spacing
    df.at[0, "gill_color"] =gill_color
    df.at[0, "stem_height"] =stem_height
    df.at[0, "stem_width"] =stem_width
    df.at[0, "stem_root"] =stem_root
    df.at[0, "stem_surface"] =stem_surface
    df.at[0, "stem_color"] =stem_color
    df.at[0, "veil_color"] =veil_color
    df.at[0, "has_ring"] =has_ring
    df.at[0, "ring_type"] =ring_type
    df.at[0, "spore_print_color"] =spore_print_color
    df.at[0, "habitat"] =habitat
    df.at[0, "season"] =season
    
    result = pipeline.predict(df)
    return result[0]
    
    
def main():
    cap_diameter = st.slider("cap_diameter", min_value=0.01, max_value=55, step=0.01, value=6.19)
    cap_shape = st.selectbox("cap_shape", min_value=0.0, max_value=850000.0, step=20.5, value=107188.0)
    R = st.slider("Radius", min_value=0.0, max_value=1950.0, step=0.05, value=237.0)
    A_M = st.slider("Abslute Magnitute", min_value=-12.0, max_value=21.0, step=0.1, value=4.3)
    Color = st.selectbox("Color", colors_inputs)
    Spectral_Class = st.selectbox("Spectral_Class", Spectral_Class_inputs)
    if st.button("Predict"):
        result = prediction(Temperature, L, R, A_M, Color, Spectral_Class)
        st.text(f"The Predicted Type is : {labelencoder.inverse_transform([result])[0]}")
        

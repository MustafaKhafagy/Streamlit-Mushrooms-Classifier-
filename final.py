
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
    cap_diameter = st.slider("Cap Diameter", min_value=0.01, max_value=55, step=0.01, value=6.19)
    cap_shape = st.selectbox("Cap Shape", ["bell", "conical", "convex", "flat","sunken", "spherical", "others" , "unkown"] )
    cap_surface = st.selectbox("Cap Surface", [ "fibrous", "grooves", "scaly", "smooth","shiny", "leathery", "silky", "sticky",
                                               "wrinkled", "fleshy" ,"unkown"])
    cap_color = st.selectbox("Cap Color", ["brown", "buff", "gray", "green", "pink","purple", "red", "white", "yellow", "blue","orange",
                                           "black" ,"unkown"])
    does_bruise_or_bleed = st.checkbox("Does it cause Bruise or Bleed ?")
    gill_attachment = st.selectbox("Gill Attachment", ["adnate", "adnexed", "decurrent", "free","sinuate", "pores", "none", "unkown"])
    gill_spacing= st.selectbox("Gill Spacing", ["close", "distant", "none"])
    gill_color = st.selectbox("Gill Color", ["brown", "buff", "gray", "green", "pink","purple", "red", "white", "yellow", "blue","orange",
                                           "black" , "none" , "unkown"])
    stem_height = st.slider("Stem Height",  min_value=0.5, max_value=50, step=0.1, value=6.4)
    stem_width = st.slider("Stem Width", min_value=0.3, max_value=100, step=0.1, value=10.8)
    stem_root= st.selectbox("Stem Root" , ["bulbous", "swollen", "club", "cup", "equal","rhizomorphs", "rooted"])
    stem_surface = st.selectbox("Stem Surface" , [ "fibrous", "grooves", "scaly", "smooth","shiny", "leathery", "silky", "sticky",
                                               "wrinkled", "fleshy" ,"unkown"])
    stem_color = st.selectbox("Stem Color" , ["brown", "buff", "gray", "green", "pink","purple", "red", "white", "yellow", "blue","orange",
                                           "black" ,"unkown"])
    veil_color = st.selectbox("Veil Color" , ["brown", "buff", "gray", "green", "pink","purple", "red", "white", "yellow", "blue","orange",
                                           "black" ,"unkown"]
    has_ring = st.checkbox("Does the Mushroom has Ring ?")
    ring_type = st.selectbox("Ring type" , ["cobwebby", "evanescent", "flaring", "grooved",
                                            "large", "pendant", "sheathing", "zone", "scaly", "movable", "none", "unknown"])
    spore_print_color =st.selectbox("Spore Print Color" , ["brown", "buff", "gray", "green", "pink","purple", "red", "white", "yellow", "blue","orange",
                                           "black" ,"unkown"])
    habitat = st.selectbox("Habitat" , [ "grasses", "leaves", "meadows" ,"paths", "heaths","urban", "waste", "woods"])
    season = st.selectbox("Season" , [ "spring", "summer", "autumn", "winter" ])
    if st.button("Predict"):
        result = prediction(cap_diameter, cap_shape, cap_surface, cap_color,oes_bruise_or_bleed, gill_attachment, gill_spacing, gill_color,
                stem_height, stem_width, stem_root, stem_surface, stem_color,
                veil_color, has_ring, ring_type, spore_print_color, habitat,season)
        if result[0] == 0 :
            
            st.text(f"This Mushroom is : Edible")
        if result[0]== 1 :
            st.text(f"This Mushroom is : Poisonous")
            

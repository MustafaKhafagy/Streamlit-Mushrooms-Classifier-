
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load pre-trained pipeline and column names
inputs = joblib.load("columns_name.pkl")
pipeline = joblib.load("pipeline.pkl")

# Streamlit app header and images
st.header("       Mushroom Classifier")

col1, col2 = st.columns(2)
with col1:
    st.header("Is it POISONOUS?")
    st.image("attachment-mushroom-feature-1.jpg")
with col2:
    st.header("Is it EDIBLE?")
    st.image("_WP__fall-mushroom-puffball-1920x1435.jpeg")

# Mapping dictionaries
mapping_dict = {
    "cap_shape": {"bell": "b", "conical": "c", "convex": "x", "flat": "f", "sunken": "s", "spherical": "p", "others": "o"},
    "cap_surface": {"fibrous": "i", "grooves": "g", "scaly": "y", "smooth": "s", "shiny": "h", "leathery": "l",
                    "silky": "k", "sticky": "t", "wrinkled": "w", "fleshy": "e"},
    "cap_color": {"brown": "n", "buff": "b", "gray": "g", "green": "r", "pink": "p", "purple": "u",
                  "red": "e", "white": "w", "yellow": "y", "blue": "l", "orange": "o", "black": "k"},
    "does_bruise_or_bleed": {True: "t", False: "f"},
    "gill_attachment": {"adnate": "a", "adnexed": "x", "decurrent": "d", "free": "e", "sinuate": "s", "pores": "p", "none": "f"},
    "gill_spacing": {"close": "c", "distant": "d", "none": "f"},
    "gill_color": {"brown": "n", "buff": "b", "gray": "g", "green": "r", "pink": "p", "purple": "u",
                   "red": "e", "white": "w", "yellow": "y", "blue": "l", "orange": "o", "black": "k"},
    "stem_root": {"bulbous": "b", "swollen": "s", "club": "c", "cup": "u", "equal": "e", "rhizomorphs": "z", "rooted": "r"},
    "stem_surface": {"fibrous": "i", "grooves": "g", "scaly": "y", "smooth": "s", "shiny": "h", "leathery": "l",
                     "silky": "k", "sticky": "t", "wrinkled": "w", "fleshy": "e"},
    "stem_color": {"brown": "n", "buff": "b", "gray": "g", "green": "r", "pink": "p", "purple": "u",
                   "red": "e", "white": "w", "yellow": "y", "blue": "l", "orange": "o", "black": "k"},
    "veil_color": {"brown": "n", "buff": "b", "gray": "g", "green": "r", "pink": "p", "purple": "u",
                   "red": "e", "white": "w", "yellow": "y", "blue": "l", "orange": "o", "black": "k"},
    "has_ring": {True: "t", False: "f"},
    "ring_type": {"cobwebby": "c", "evanescent": "e", "flaring": "r", "grooved": "g", "large": "l",
                  "pendant": "p", "sheathing": "s", "zone": "z", "scaly": "y", "movable": "m", "none": "f", "unknown": np.nan},
    "spore_print_color": {"brown": "n", "buff": "b", "gray": "g", "green": "r", "pink": "p", "purple": "u",
                          "red": "e", "white": "w", "yellow": "y", "blue": "l", "orange": "o", "black": "k"},
    "habitat": {"grasses": "g", "leaves": "l", "meadows": "m", "paths": "p", "heaths": "h", "urban": "u", "waste": "w", "woods": "d"},
    "season": {"spring": "s", "summer": "u", "autumn": "a", "winter": "w"}
}

def prediction(cap_diameter, cap_shape, cap_surface, cap_color, does_bruise_or_bleed, gill_attachment, gill_spacing, gill_color,
                stem_height, stem_width, stem_root, stem_surface, stem_color,
                veil_color, has_ring, ring_type, spore_print_color, habitat, season):
    
    # Map input values using mapping_dict
    cap_shape = mapping_dict["cap_shape"][cap_shape]
    cap_surface = mapping_dict["cap_surface"][cap_surface]
    cap_color = mapping_dict["cap_color"][cap_color]
    does_bruise_or_bleed = mapping_dict["does_bruise_or_bleed"][does_bruise_or_bleed]
    gill_attachment = mapping_dict["gill_attachment"][gill_attachment]
    gill_spacing = mapping_dict["gill_spacing"][gill_spacing]
    gill_color = mapping_dict["gill_color"][gill_color]
    stem_root = mapping_dict["stem_root"][stem_root]
    stem_surface = mapping_dict["stem_surface"][stem_surface]
    stem_color = mapping_dict["stem_color"][stem_color]
    veil_color = mapping_dict["veil_color"][veil_color]
    has_ring = mapping_dict["has_ring"][has_ring]
    ring_type = mapping_dict["ring_type"][ring_type]
    spore_print_color = mapping_dict["spore_print_color"][spore_print_color]
    habitat = mapping_dict["habitat"][habitat]
    season = mapping_dict["season"][season]

    
    df = pd.DataFrame([[cap_diameter, cap_shape, cap_surface, cap_color,
                        does_bruise_or_bleed, gill_attachment, gill_spacing, gill_color,
                        stem_height, stem_width, stem_root, stem_surface, stem_color,
                        veil_color, has_ring, ring_type, spore_print_color, habitat, season]],
                      columns=inputs)
    
    # Predict using the pipeline
    result = pipeline.predict(df)
    return result[0]

def main():
    try:
        cap_diameter = st.slider("Cap Diameter", min_value=0.01, max_value=55.0, step=0.01, value=6.19)
        cap_shape = st.selectbox("Cap Shape", ["bell", "conical", "convex", "flat", "sunken", "spherical", "others"])
        cap_surface = st.selectbox("Cap Surface", ["fibrous", "grooves", "scaly", "smooth", "shiny", "leathery", "silky", "sticky",
                                                   "wrinkled", "fleshy"])
        cap_color = st.selectbox("Cap Color", ["brown", "buff", "gray", "green", "pink", "purple", "red", "white", "yellow", "blue", "orange",
                                               "black"])
        does_bruise_or_bleed = st.checkbox("Does it cause Bruise or Bleed?  # Select if True")
        gill_attachment = st.selectbox("Gill Attachment", ["adnate", "adnexed", "decurrent", "free", "sinuate", "pores", "none"])
        gill_spacing = st.selectbox("Gill Spacing", ["close", "distant", "none"])
        gill_color = st.selectbox("Gill Color", ["brown", "buff", "gray", "green", "pink", "purple", "red", "white", "yellow", "blue", "orange",
                                                 "black"])
        stem_height = st.slider("Stem Height", min_value=0.5, max_value=50.0, step=0.1, value=6.4)
        stem_width = st.slider("Stem Width", min_value=0.3, max_value=100.0, step=0.1, value=10.8)
        stem_root = st.selectbox("Stem Root", ["bulbous", "swollen", "club", "cup", "equal", "rhizomorphs", "rooted"])
        stem_surface = st.selectbox("Stem Surface", ["fibrous", "grooves", "scaly", "smooth", "shiny", "leathery", "silky", "sticky",
                                                     "wrinkled", "fleshy"])
        stem_color = st.selectbox("Stem Color", ["brown", "buff", "gray", "green", "pink", "purple", "red", "white", "yellow", "blue", "orange",
                                                 "black"])
        veil_color = st.selectbox("Veil Color", ["brown", "buff", "gray", "green", "pink", "purple", "red", "white", "yellow", "blue", "orange",
                                                 "black"])
    
        has_ring = st.checkbox("Does the Mushroom have a Ring?")
        if has_ring:
            ring_type = st.selectbox("Ring Type", ["cobwebby", "evanescent", "flaring", "grooved",
                                                   "large", "pendant", "sheathing", "zone", "scaly", "movable","unkown"])
        else:
            ring_type = "none"
        spore_print_color = st.selectbox("Spore Print Color", ["brown", "buff", "gray", "green", "pink", "purple", "red", "white", "yellow", "blue", "orange",
                                                               "black"])
        habitat = st.selectbox("Habitat", ["grasses", "leaves", "meadows", "paths", "heaths", "urban", "waste", "woods"])
        season = st.selectbox("Season", ["spring", "summer", "autumn", "winter"])
        
        if st.button("Predict"):
            result = prediction(cap_diameter, cap_shape, cap_surface, cap_color, does_bruise_or_bleed, gill_attachment, gill_spacing, gill_color,
                                stem_height, stem_width, stem_root, stem_surface, stem_color,
                                veil_color, has_ring, ring_type, spore_print_color, habitat, season)
            if result == 0:
                st.text("This Mushroom is: Edible")
                st.image("right sign.jpg" , width=200 )
            elif result == 1:
                st.text("This Mushroom is: Poisonous")
                st.image("poison-warning-sign.jpg" , width = 200)
                
    except Exception as e:
        st.error(f"An error occurred: {str(e)}. Please check your inputs and try again.")
        
main()

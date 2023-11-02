import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox("Select animal type", ("dog", "cat", "bird", "fish", "reptile"))

if animal_type == "cat":
    pet_color = st.sidebar.text_area(label="Select cat color", max_chars=15, value="calico")
elif animal_type == "dog":
    pet_color = st.sidebar.text_area(label="Select dog color", max_chars=15, value="black")
elif animal_type == "bird":
    pet_color = st.sidebar.text_area(label="Select bird color", max_chars=15, value="blue")
elif animal_type == "fish":
    pet_color = st.sidebar.text_area(label="Select fish color", max_chars=15, value="orange")
elif animal_type == "reptile":
    pet_color = st.sidebar.text_area(label="Select reptile color", max_chars=15, value="green")

if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.text (response)

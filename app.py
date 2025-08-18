import streamlit as st
import random
from main import expand_prompt, call_api
from pallate import generate_random_palette

st.set_page_config(page_title="Q&A App", page_icon="❓")

st.title("Moodboard Generator")

reference_prompt = open('prompt_text.txt', "r").read()
color_pallate = generate_random_palette(random.randint(3,6))



def list_to_string(lst, separator = " "):
    return separator.join(lst[1:])


labels = [
    "Service: ",
    "Sub-service: ",
    "Style: ", 
    "Application: ",
    "Project Breif:"]

values = ["Graphics Desgin",
             "Poster/Flyer",
             "Minimal"
             "Print",
             "This is for opening of a new coffe shop"]

pallate = list_to_string(color_pallate)

reference_prompt = reference_prompt + "\n\n" + pallate

if st.button("Submit"):
    saved_questions = [q for q in values if q.strip()]

    prompt1 = expand_prompt(list_to_string(labels, "\n"), list_to_string(values, " \n "), reference_prompt)
    prompt2 = expand_prompt(list_to_string(labels, "\n"), list_to_string(values, " \n "), reference_prompt)

    response1 = call_api(prompt1)
    response2 = call_api(prompt2)

    st.subheader("Generated Image")
    data = response1.json() 
    image_url1 = data['data'][0]['url']

    st.subheader("Generated Image")
    data = response2.json() 
    image_url2 = data['data'][0]['url']

    col1, col2 = st.columns(2)

    with col1:
        st.image(image_url1, caption="Generated Image 1", use_container_width=True)
        if st.button("Choose Image 1", key="choose_1"):
            st.session_state.selected_image = image_url1
            st.success("✅ Image 1 selected!")

    with col2:
        st.image(image_url2, caption="Generated Image 2", use_container_width=True)
        if st.button("Choose Image 2", key="choose_2"):
            st.session_state.selected_image = image_url2
            st.success("✅ Image 2 selected!")

    if "selected_image" in st.session_state:
            st.subheader("Your Selection")
            st.image(st.session_state.selected_image, caption="Selected Mood Board", use_container_width=True)








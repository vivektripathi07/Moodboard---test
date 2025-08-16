import streamlit as st
from main import expand_prompt, call_api

st.set_page_config(page_title="Q&A App", page_icon="❓")

st.title("Question Answering App")

reference_prompt = open('prompt_text.txt', "r").read()

def list_to_string(lst, separator = " "):
    return separator.join(lst[1:])

labels = [
    "Enter the main prompt: ",
    "Give some keywords which sets the tone: ",
    "Give color or color pallates: ", 
    "Give some keywords for textures: ",
    "How many images sections should it have: "]

questions = []
for label in labels:
    q = st.text_area(f"{label}:", placeholder=f"Enter..")
    questions.append(q)

if st.button("Submit"):
    saved_questions = [q for q in questions if q.strip()]

    finalPrompt = expand_prompt(questions[0], list_to_string(questions, " | "), reference_prompt)
    st.write(finalPrompt)

    response = call_api(finalPrompt)

    st.subheader("Generated Image")
    data = response.json() 
    image_url = data['data'][0]['url']
    st.image(image_url, caption="Generated Mood Board", use_container_width=True)

    if saved_questions:
        st.write()
    else:
        st.warning("Kindly enter")







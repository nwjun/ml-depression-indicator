import sys
import streamlit as st
from constant import recommendationForm
sys.path.append('./model')
from Recommendation import Recommendation
from PIL import Image

st.set_page_config(
    page_title="Stress Relieve Recommendation",
    page_icon="📝",
)

@st.cache
def predict(model, answer):
    return model.predict(answer)

st.header("Stress Relieve Recommendation")
model = Recommendation("./model/Recommendation.h5")
answer = [None] * len(recommendationForm)

print(answer)

with st.form("my_form"):
    for idx, i in enumerate(recommendationForm):
        if 'image' in i.keys():
            image = Image.open(i['image'])
            st.image(image)
        type = i['type']
        if type == 0:
            answer[idx] = st.radio(i['question'], i['options'], key=idx)
        elif type == 1:
            answer[idx] = st.selectbox(i["question"], i['options'], key=idx)
        elif type == 2:
            answer[idx] = st.multiselect(i["question"], i['options'], key=idx)
        elif type == 3:
            answer[idx] = st.slider(i["question"], **i["kwargs"], key=idx)
        elif type == 4:
            answer[idx] = st.select_slider(i["question"], i["option"], key=idx)
        elif type == 5:
            answer[idx] = st.text_input(i['question'], key=idx)
        elif type == 6:
            answer[idx] = st.number_input(
                i['question'], key=idx,  **i['kwargs'])
        elif type == 7:
            answer[idx] = st.text_area(i['question'], key=idx)
    
    submitted = st.form_submit_button("Submit")

    if submitted:
        prediction, suggestion = predict(model, answer)
        st.write(f'Predicted: %s' % prediction)
        for i in range(len(suggestion)):
            st.write("Suggestion Top " + str(i+1) + ": " + suggestion[i])

import sys
import streamlit as st
import numpy as np
from constant import recommendationForm
from constant import depression_questionnaire
from pageController import PageController
sys.path.append('./model')
from depressionModel import DepressionModel

# To add question, add in 'constant.py'


def depressionTest():
    st.subheader("Depression questionnaire")

    depressionAnswer = [None] * len(depression_questionnaire)
    with st.form("my_form"):
        for idx, i in enumerate(depression_questionnaire):
            depressionAnswer[idx] = 1 if st.radio(
                i['question'], i['options'], key=idx) == "Yes" else 0

        submitted = st.form_submit_button("Submit")

        if submitted:
            depression = DepressionModel("./model/depressionModel.sav")
            isDepressed = depression.predict(depressionAnswer)
            st.write(f"You are {'depressed' if isDepressed else 'not depressed'}")


def recommendationSys():
    st.subheader("Stress Relieve Recommendation")

    answer = [None] * len(recommendationForm)

    for idx, i in enumerate(recommendationForm):
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


app = PageController()

app.add_page("Depression questionnaire", depressionTest)
app.add_page("Stress Relieve Recommendation", recommendationSys)

app.run()

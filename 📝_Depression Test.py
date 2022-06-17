import sys
import streamlit as st
from constant import depression_questionnaire
sys.path.append('./model')
from depressionModel import DepressionModel

st.set_page_config(
    page_title="Depression Test",
    page_icon="📝",
)

@st.cache
def predict(model, answer):
    return model.predict(answer)

st.header("Depression questionnaire")

depression = DepressionModel("./model/DepressionDL_v1.h5")
depressionAnswer = [None] * len(depression_questionnaire)

with st.form("my_form"):
    for idx, i in enumerate(depression_questionnaire):
        depressionAnswer[idx] = 1 if st.radio(
            i['question'], i['options'], key=idx) == "Yes" else 0

    submitted = st.form_submit_button("Submit")

    if submitted:
        isDepressed, confidence = predict(depression, depressionAnswer)
        st.write(f"You are {'depressed' if isDepressed else 'not depressed'}")
        st.write(f"Confidence: {'{:.2f}'.format(float((confidence)*100)) if isDepressed else '{:.2f}'.format(float((1-confidence)*100))}%")


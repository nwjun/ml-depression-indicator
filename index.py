import streamlit as st
from constant import recommendationForm 

st.title('Depression Indicator')

# Depression Indicator
st.subheader("Depression questionnaire")



# Stress Relieve Recommendation
st.subheader("Stress Relieve Recommendation")

# To add question, add in 'constant.py'
answer = [None]* len(recommendationForm)

print(len(recommendationForm))
for idx, i in enumerate(recommendationForm):
    type = i['type']
    print(recommendationForm)
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
        answer[idx] = st.number_input(i['question'], key=idx,  **i['kwargs'])
    elif type == 7:
        answer[idx] = st.text_area(i['question'], key=idx)
    

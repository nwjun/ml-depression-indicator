"""
    type:
        0: radio
        1: selectbox
        2: multiselect
        3: slider
        4: select-slider
        5: text input
        6: number input
        7: text area
"""

depression_questionnaire = [
    {
        'question': "Are you satisfied with your current living environment?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Are you satisfied with your current position/academic achievement?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Are you suffering rom any financial stress?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Are you in any kind of debt?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Are you suffering from eating disorders like overeating or loss of appetite?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Are you suffering from insomnia?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Do you feel anxiety for something recently?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Do you feel that you deprived of something that you deserve recently?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Do you feel that you are abused (physcially, sexually, mentally) recently?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Do you feel that you are cheated by someone recently?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Have you faced any life-threatening event recently?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Do you have suicidal thoughts recently?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Are you suffering from inferiority complex recently?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Do you engage yourself in any kind of conflicts with your friends or family recently?",
        'options': ["Yes","No"],
        'type': 0,
    },
    {
        'question': "Do you lost someone who is close to you recently?",
        'options': ["Yes","No"],
        'type': 0,
    },
]

"""
    type:
        0: radio
        1: selectbox
        2: multiselect
        3: slider
        4: select-slider
        5: text input
        6: number input
        7: text area
"""


recommendationForm = [
    {
        'question': "Gender",
        'options': ["Male", "Female"],
        'type': 1,
    },
    {
        'question': "How energetic are you?",
        'image': './images/Q1.png',
        'options': ["Extraverts - E", "Introverts - I"],
        'type': 1,
    },
    {
        'question': "How do you see the world & gather information?",
        'image': './images/Q2.png',
        'options': ["Sensors - S", "Intuitives - N"],
        'type': 1,
    },
    {
        'question': "How do you make your decisions?",
        'image': './images/Q3.png',
        'options': ["Thinkers - T", "Feelers - F"],
        'type': 1,
    },
    {
        'question': "How much do you like to plan ahead?",
        'image': './images/Q4.png',
        'options': ["Judgers - J", "Perceivers - P"],
        'type': 1,
    },
    {
        'question': "Who are you?",
        'image': './images/Personalities.png',
        'options': ["Analyst(Purple)", "Diplomat(Green)", "Sentinel(Blue)", "Explorer(Red)"],
        'type': 1,
    },
    {
        'question': "How do you want to feel for stress relieve activities?",
        'options': ["Happy and carefree", "Calm and creative", "Healthy and satisfied", "Productive and progressing"],
        'type': 1,
    },
    {
        'question': "Do you prefer indoor or outdoor hobbies?",
        'options': ['Outdoors', 'Indoors', 'Both', 'It doesn\'t matter'],
        'type':1,
    },
    {
        'question': 'Do you feel happier when you consume or when you create something?',
        'options': ['I feel better when I create', 'I feel better when I consume', 'Both', 'I dislike both'],
        'type': 1,
    },
]

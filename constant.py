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

recommendationForm = [
    {
        'question': "Hi how are you",
        'options': ["test1", "test2", "test3"],
        'type': 1,
    },
    {
        'question': "Hi how are you",
        'type': 6,
        'kwargs': {
            'min_value': 0,
            'max_value': 10
        }
    }
]

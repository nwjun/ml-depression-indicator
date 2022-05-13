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

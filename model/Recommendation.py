import numpy as np
import tensorflow as tf

class Recommendation:
    def __init__(self,filename):
        self.model = tf.keras.models.load_model(filename)


    def predict(self, array):
        # Manual One-hot Encoding Rules       
        energetic = ["Extraverts - E", "Introverts - I"]
        energetic_to_num = dict((c, i) for i, c in enumerate(energetic))
        num_to_energetic = dict((i, c) for i, c in enumerate(energetic))

        sense = ["Sensors - S", "Intuitive - N"]
        sense_to_num = dict((c, i) for i, c in enumerate(sense))
        num_to_sense = dict((i, c) for i, c in enumerate(sense))

        decision = ["Thinkers - T", "Feelers - F"]
        decision_to_num = dict((c, i) for i, c in enumerate(decision))
        num_to_decision = dict((i, c) for i, c in enumerate(decision))

        plan = ["Judgers - J", "Perceivers - P"]
        plan_to_num = dict((c, i) for i, c in enumerate(plan))
        num_to_plan = dict((i, c) for i, c in enumerate(plan))

        behaviour = ["Analyst (Purple)", "Diplomat (Green)", "Sentinel (Blue)", "Explorer (Red)"]
        behaviour_to_num = dict((c, i) for i, c in enumerate(behaviour))
        num_to_behaviour = dict((i, c) for i, c in enumerate(behaviour))

        activities_type = ["Happy and carefree", "Calm and creative", "Healthy and satisfied", "Productive and progressing"]
        actType_to_num = dict((c, i) for i, c in enumerate(activities_type))
        num_to_actType = dict((i, c) for i, c in enumerate(activities_type))

        inout = ["Outdoors", "Indoors", "Both", "It doesn't matter"]
        inout_to_num = dict((c, i) for i, c in enumerate(inout))
        num_to_inout = dict((i, c) for i, c in enumerate(inout))

        cc = ["I feel better when I create", "I feel better when I consume", "Both", "I dislike both"]
        cc_to_num = dict((c, i) for i, c in enumerate(cc))
        num_to_cc = dict((i, c) for i, c in enumerate(cc))

        gender = ["Male", "Female"]
        gender_to_num = dict((c, i) for i, c in enumerate(gender))
        num_to_gender = dict((i, c) for i, c in enumerate(gender))

        depActivities = ["Meditation", "Religious Prayer", "Yoga", "Journaling", "Enjoy good food", "Resting - Sleep", "Creating Art", "Exercise", "Diet", "Spending time with loved ones", "Confess to family or loved ones (without hiding anything)", "Baking", "Reading", "Watch movies/ anime/ series", "Listen to music", "Enjoying the nature", "Attend counseling session", "Consult with doctor", "Gaming", "Shopping", "Travelling", "Playing musical instruments"]
        depActivities_to_num = dict((c, i) for i, c in enumerate(depActivities))
        num_to_depActivities = dict((i, c) for i, c in enumerate(depActivities))

        userInput = []
        userInput.append(energetic_to_num[array[0]])
        userInput.append(sense_to_num[array[1]])
        userInput.append(decision_to_num[array[2]])
        userInput.append(plan_to_num[array[3]])
        userInput.append(behaviour_to_num[array[4]])
        userInput.append(actType_to_num[array[5]])
        userInput.append(inout_to_num[array[6]])
        userInput.append(cc_to_num[array[7]])
        userInput.append(gender_to_num[array[8]])

        print(userInput)
        print(userInput)
        print(userInput)
        print(userInput)
        print(userInput)
        print(userInput)
        print(userInput)
        print(userInput)
        
        yhat = self.model.predict(np.asarray([userInput]))
        predict = np.argpartition(yhat[0], -4)[-4:]
        result = np.round(yhat, decimals=2, out=None)
        print('Predicted: %s' % np.round(yhat, decimals=2, out=None))

        suggestion = []
        for i, j in enumerate(predict):
            suggestion.append(depActivities[j])
            print("Suggestion Top " + str(i+1) + ": " + depActivities[j])

        return result, suggestion

    

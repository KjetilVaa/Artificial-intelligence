from sklearn import tree
import numpy as np

# Ignore deprecation warnings since this file will not be updated.
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# [height, weight, shoe, size]

# Random data sets to train learning model

X = [[181, 80, 40], [175, 75, 43], [160, 70, 37], [194, 89, 45], [72, 72, 40], [182, 82, 44], [159, 62, 37]]

Y = ["male", "male", "female", "male", "female", "male", "female"]


# Validation
def inputValidation(input):
    if int(input) > 0:
        return True
    else:
        return False


# classifier

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

while True:
    print("Please enter det requested information to test the decision tree model:")
    validInput = True
    height = input("Height: ")
    weight = input("Weight: ")
    shoe_size = input("Shoe size: ")
    prediction = [height, weight, shoe_size]
    for o in prediction:
        if not inputValidation(o):
            validInput = False
            print("Invalid input. Please try again with positive integers!")
            continue
    if validInput:
        result = clf.predict(np.array(prediction).reshape(1, -1))
        print("RESULT ----> ", result[0].upper())
        print("--------------------------------")

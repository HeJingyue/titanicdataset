import streamlit as st
import pickle

st.title("Kat's Titanic Prediction App!")
st.image('titanic2.jpeg')
picke_in = open('titanicdataset.pkl', 'rb')
classifier = pickle.load(picke_in)

#Defining the function which will make the prediction using the data that user will input
def prediction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    prediction = classifier.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
    print(prediction)
    return prediction

def main():
    st.title("Titanic Prediction App!")

    #The following code creates textboxes in which the user can enter the data required to make prediction
    Pclass = st.text_input("Passenger Class")
    Sex = st.text_input("Sex")
    Age = st.text_input("Age")
    SibSp = st.text_input("SibSp")
    Parch = st.text_input("Parch")
    Fare = st.text_input("Fare")
    Embarked = st.text_input("Embarked")
    result = ""
    #The below code ensures that when the button 'Predict' is clicked, the prediction function defined
    #above is called to make the prediction and store it in the variable result
    
    if st.button("Predict"):

        #Convert inputs to appropriate types
        Pclass = int(Pclass)
        Age = float(Age)
        SibSp = int(SibSp)
        Parch = int(Parch)
        Fare = float(Fare)

        result = prediction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
    st.success("This output is: {}".format(result))


main()
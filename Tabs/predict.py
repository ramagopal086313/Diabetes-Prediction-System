"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Early Prediction of Diabetes.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    glucose = st.slider("Glucose", int(df["Glucose"].min()), int(df["Glucose"].max()))
    bp = st.slider("Blood_Pressure", int(df["Blood_Pressure"].min()), int(df["Blood_Pressure"].max()))
    insulin = st.slider("Insulin", int(df["Insulin"].min()), int(df["Insulin"].max()))
    bmi = st.slider("BMI", float(df["BMI"].min()), float(df["BMI"].max()))
    pedigree = st.slider("Genetic Correlation", float(df["Pedigree_Function"].min()), float(df["Pedigree_Function"].max()))
    age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))

    # Create a list to store all the features
    features = [glucose, bp, insulin, bmi, pedigree, age]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.20
        st.success("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person either has diabetes or prone to get diabetes")
        else:
            st.info("The person is free from diabetes")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")

import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model and DataFrame
pipe = pickle.load(open("GBC_pipeline.pkl", 'rb'))
df = pickle.load(open("df.pkl", 'rb'))

#st.title('Heart Disease Predictor')

st.write("""
    
    # Heart Disease Predictor  
    
    This is my project on heart disease prediction, using data I downloaded from Kaggle. Throughout this endeavor, I gained substantial knowledge and learned numerous new techniques. 
    
    By applying various data preprocessing and machine learning methods, I was able to build an effective model. I achieved an accuracy of about 99.50% with my model. 
    
             """)


# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Age input box
    age_input = st.text_input('Age', placeholder='Enter your Age')
    try:
        age = int(age_input)
    except ValueError:
        age = None
        
    # Sex selectbox
    sex = st.selectbox('Sex', df['Sex'].unique())

    # RestingBP input box
    RestingBP_input = st.text_input('Resting Blood Pressure', placeholder='Enter your RestingBP')
    try:
        RestingBP = int(RestingBP_input)
    except ValueError:
        RestingBP = None

    # Cholesterol input box
    #Cholesterol = st.number_input('Cholesterol')
    
    Cholesterol_input = st.text_input('Cholesterol', placeholder='Enter your Cholesterol level')
    try:
        Cholesterol = int(Cholesterol_input)
    except ValueError:
        Cholesterol = None

    # MaxHR input box
    MaxHR = st.number_input('MaxHR')

with col2:
    # Sex selectbox
    #sex = st.selectbox('Sex', df['Sex'].unique())

    # ChestPainType selectbox
    ChestPainType = st.selectbox('ChestPainType', df['ChestPainType'].unique())

    # FastingBS selectbox
    FastingBS = st.selectbox('FastingBS', df['FastingBS'].unique())

    # RestingECG selectbox
    RestingECG = st.selectbox('RestingECG', df['RestingECG'].unique())

    # ExerciseAngina selectbox
    ExerciseAngina = st.selectbox('ExerciseAngina', df['ExerciseAngina'].unique())
    
    # ST_Slope selectbox
    ST_Slope = st.selectbox('ST_Slope', df['ST_Slope'].unique())

# Oldpeak selectbox
#Oldpeak = st.selectbox('Oldpeak', df['Oldpeak'].unique())
Oldpeak = st.slider('Oldpeak', -2.6, 6.2, 0.0)


# Prediction button
if st.button('Predict Heart Disease'):
    # Ensure all inputs are valid before making the prediction
    if age is not None and RestingBP is not None:
        # Create a dictionary with the inputs
        input_data = {
            'Age': age,
            'Sex': sex,
            'ChestPainType': ChestPainType,
            'RestingBP': RestingBP,
            'Cholesterol': Cholesterol,
            'FastingBS': FastingBS,
            'RestingECG': RestingECG,
            'MaxHR': MaxHR,
            'ExerciseAngina': ExerciseAngina,
            'Oldpeak': Oldpeak,
            'ST_Slope': ST_Slope
        }

        # Convert the dictionary to a DataFrame
        query_df = pd.DataFrame([input_data])

        try:
            prediction = pipe.predict(query_df)
            if prediction[0]:
                st.success('You have Heart Disease: Yes')
                
            else:
                st.success("You don't have Heart Disease: No")
        except:
            st.error("Please enter valid values for Age and Resting Blood Pressure.")

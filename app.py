import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image


pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Cardiac Prediction"


def predict_note_authentication(age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active):
    
    prediction=classifier.predict([[age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active]])
    print(prediction)
    return prediction

def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Cardiovascular Disease Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
   
    age = st.slider("Age", 1, 100,1)

    gender = st.selectbox("Gender",options=['Male' , 'Female'])
  
    weight = st.slider("Weight(kg)", 50, 200,60)
    height = st.slider("Height(cm)", 100, 200,170)
    
    ap_hi = st.slider("Systolic blood pressure",50,190,120, step = 10)
    ap_lo = st.slider("Diastolic blood pressure",50,190,100, step = 10)
    
    chol = st.selectbox("Cholesterol level",options=['Normal' , 'Above normal','Well above normal'])
    gluc = st.selectbox("Glucose level",options=['Normal' , 'Above normal','Well above normal'])
    
    smoke = st.selectbox("Are you a Smoker?",options=['Yes' , 'No'])
    
    alco = st.selectbox("Do you drink alcohol often?",options=['Yes' , 'No'])
    
    
    active = st.selectbox("Do you excersice at least 3 times in a week?",options=['Yes' , 'No'])   
    
    gender = 0 if gender == 'Male' else 1
    
    
    cholesterol = 1
    if chol == 'Normal':
        cholesterol = 1
    elif chol == 'Above normal':
        cholesterol = 2
    else:
        cholesterol = 3
        
    
    gluc = 1
    if gluc == 'Normal':
        gluc = 1
    elif gluc == 'Above normal':
        gluc = 2
    else:
        gluc = 3

    smoke = 1 if smoke == 'Yes' else 1
    alco = 1 if alco == 'Yes' else 1
    active = 1 if active == 'YesS' else 1

        
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active)
        if result == 0:
            st.subheader('You will not have Cardiovascular Disease')
        else:
            st.subheader('It is probable that you will have Cardiovascular Disease in future, Please consult your doctor.')   
    
if __name__=='__main__':
    main()
    
    
    
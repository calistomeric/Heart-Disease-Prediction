# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 05:10:35 2023

@author: cali
"""

import streamlit as st
import pickle
import base64
pickled_model = pickle.load(open('model.pkl', 'rb'))

def welcome():
    return 'Welcome All'

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    prediction = pickled_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]
    return prediction

def main():
    st.title('Heart Disease Predictor')
    html_temp = """
    <div style='background-color:tomato; background-image: url('heart_disease.jpg'); padding:10px'>
    <h2 style='color:white; text-align:center'>Heart Disease Predicting App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    ############## for background image #################
    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
            return base64.b64encode(data).decode()
        
    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)
    set_background('heart_disease.jpg')
    ############# for background image ###################
    
    age = st.text_input('age')
    
    sex = st.selectbox('sex', ('Male', 'Female'))
    if sex == 'Male':
        sex = 1
    elif sex == 'Female':
        sex = 0
        
    cp = st.selectbox('chest pain type', ('typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'))
    if cp == 'typical angina':
        cp = 1
    elif cp == 'atypical angina':
        cp = 2
    elif cp == 'non-anginal pain':
        cp = 3
    elif cp == 'asymptomatic':
        cp=4
        
    trestbps = st.text_input('resting blood pressure (in mm Hg)')
    
    chol = st.text_input('serum cholestoral (in mg/dl)')
    
    fbs = st.selectbox('fasting blood sugar (>120 mg/dl)', ('True', 'False'))
    if fbs == 'True':
        fbs = 1
    elif fbs == 'False':
        fbs = 0
        
    restecg = st.selectbox('resting ecg results', ('normal', 'ST-T wave abnormality', 'ventricular hypertrophy by Estes criteria'))
    if restecg == 'normal':
        restecg = 0
    elif restecg == 'ST-T wave abnormality':
        restecg = 1
    elif restecg == 'ventricular hypertrophy by Estes criteria':
        restecg = 2
        
    thalach = st.text_input('maximum heart rate achieved')
    
    exang = st.selectbox('exercise induced angina', ('True', 'False'))
    if exang == 'True':
        exang = 1
    elif exang == 'False':
        exang = 0
    
    oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    
    slope = st.selectbox('the slope of the peak exercise ST segment', ('upsloping', 'flat', 'downsloping'))
    if slope == 'upsloping':
        slope = 1
    elif slope == 'flat':
        slope = 2
    elif slope == 'downsloping':
        slope = 3
        
    ca = st.selectbox('number of major vessels', ('0', '1', '2', '3'))
    thal = st.selectbox('thal', ('normal', 'fixed defect', 'reversable defect'))
    if thal == 'normal':
        thal = 3
    elif thal == 'fixed defect':
        thal = 6
    elif thal == 'reversable defect':
        thal = 7
    
    result=0
    heart_disease_or_not = {0: 'You do not have heart disease', 1: 'You have heart disease'}
    try:
        if st.button('Predict'):
            result = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
            result_output = ('{}'.format(heart_disease_or_not[result]))
            css_temp = f"""
            <p style='background-color:tomato; border-radius:7px; padding:10px; color:white; text-align:center;
            font-size: 18px'>{result_output}</style><BR>
            </p>
            """
            st.markdown(css_temp, unsafe_allow_html=True)
            
    except (ValueError, TypeError, NameError):
        pass
    if st.button('About'):
        st.text('''Helps you to know your heart disease status based on parameters from hospital @Calligraphy''')
        
if __name__=='__main__':
    main()
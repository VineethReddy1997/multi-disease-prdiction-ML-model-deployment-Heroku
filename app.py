## Importing Required libraries
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("diabetes_model.sav",'rb'))

heart_disease_model = pickle.load(open("heart_disease_model.sav",'rb'))

parkinsons_model = pickle.load(open("parkinson_disease_model.sav", 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using Machine Learning')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies  (Enter Numbers)')
        
    with col2:
        Glucose = st.text_input('Glucose Level  (Enter Number only)')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value  (Enter Number only)')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value  (Enter Number only)')
    
    with col2:
        Insulin = st.text_input('Insulin Level  (Enter Number only)')
    
    with col3:
        BMI = st.text_input('BMI value  (Enter Number only)')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value  (Enter Number only)')
    
    with col2:
        Age = st.text_input('Age of the Person  (Enter Number only)')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic.. please  consult a  diagnostic specialist '
        else:
            diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using Machine Learning')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age -> 1 to 100')
        
    with col2:
        sex = st.text_input('Sex -> 0 or 1')
        
    with col3:
        cp = st.text_input('Chest Pain types -> Enter(0,1,2,3)')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (Enter Number only)')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl (Enter Number only)')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (Enter Number only) ')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (Enter Number only)')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved (Enter Number only)')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina (Enter Numbers 0 or 1)')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise (Enter Numbers 0 to so on..)')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (Enter Numbers 1 or 2)')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (Enter Number in  0,1,2,3)')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect (Enter Number only)')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease Please consult cardialogyst'
        else:
            heart_diagnosis = 'The person does not have any heart disease or less chances '
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using Machine Learning")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz) (Enter Number only)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz) (Enter Number only)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz) (Enter Number only)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%) (Enter Number only)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)  (Enter Number only)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP  (Enter Number only)')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ  (Enter Number only)')
        
    with col3:
        DDP = st.text_input('Jitter:DDP  (Enter Number only)')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer  (Enter Number only)')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)  (Enter Number only)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3  (Enter Number only)')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5  (Enter Number only)')
        
    with col3:
        APQ = st.text_input('MDVP:APQ  (Enter Number only)')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA  (Enter Number only)')
        
    with col5:
        NHR = st.text_input('NHR  (Enter Number only)')
        
    with col1:
        HNR = st.text_input('HNR  (Enter Number only)')
        
    with col2:
        RPDE = st.text_input('RPDE  (Enter Number only)')
        
    with col3:
        DFA = st.text_input('DFA  (Enter Number only)')
        
    with col4:
        spread1 = st.text_input('spread1  (Enter Number only)')
        
    with col5:
        spread2 = st.text_input('spread2  (Enter Number only)')
        
    with col1:
        D2 = st.text_input('D2  (Enter Number only)')
        
    with col2:
        PPE = st.text_input('PPE  (Enter Number only)')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease Please consult a Neurologist "
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease or Decreased"
        
    st.success(parkinsons_diagnosis)


    
    
    

st.subheader('@VineethReddy Gangula ❤️😎')

#----------------------Hide Streamlit footer----------------------------
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
#--------------------------------------------------------------------
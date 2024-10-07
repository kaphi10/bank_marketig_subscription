import pandas as pd
import numpy as np
import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier


def load_model():
    with open('random_model.pickle','rb')as file:
        model=pickle.load(file)
        return model
st.header('Welcome to Marketing Application')

age=st.number_input('Enter age',min_value=15,max_value=100)
job=st.number_input('Enter job',min_value=0,max_value=11)
marital=st.number_input('Enter marital status', min_value=0,max_value=5)
education=st.number_input('Enter education')
default=st.number_input('Enter Default 1=yes,0=no')
balance=st.number_input('Enter Balance')
housing=st.number_input('Enter Housing 1=yes,0=no',max_value=1,min_value=0)
loan=st.number_input('Enter loan 1=yes,0=no',max_value=1,min_value=0)
contact=st.number_input('Enter contact ',max_value=4,min_value=1)
days=st.number_input('Enter days',max_value=31,min_value=1)
month=st.number_input('Enter month ',max_value=12,min_value=1)
duration=st.number_input('Enter duration')
campaign=st.number_input('Enter campaign')
pdays=st.number_input('Enter pdays')
previous=st.number_input('Enter previous')
poutcome=st.number_input('Enter poutcome 1=yes,0=no',max_value=3,min_value=0)

model=load_model()
def predict_subscription(input_value):
    input_value_array=np.asarray(input_value)
    reshape_input=input_value_array.reshape(1,-1)
    predicted=model.predict(reshape_input)
    # print(predicted)
    if predicted[0]==1:
        return 'Yes subscription'
    else:
        return 'No subscription '
    
def main():
    
    prediction=''
    
    if st.button('predict'):
        prediction=predict_subscription([age,job,marital,education,default,balance,
                                         housing,loan,contact,days,month,duration,
                                         campaign,pdays,previous,poutcome])
        st.success(prediction)
        
if __name__=='__main__':
    main()
    




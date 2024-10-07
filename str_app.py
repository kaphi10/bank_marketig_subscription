# import pandas as pd
import numpy as np
import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier

st.header('Welcome to Marketing Application')

age=st.number_input('Enter age',min_value=15,max_value=100)
job=st.number_input('Enter job',min_value=0,max_value=11)
marital=st.number_input('Enter marital status', min_value=0,max_value=5)
education=st.number_input('Enter education',min_value=0)
default=st.number_input('Enter Default 1=yes,0=no', min_value=0)
balance=st.number_input('Enter Balance',min_value=0)
housing=st.number_input('Enter Housing 1=yes,0=no',max_value=1,min_value=0)
loan=st.number_input('Enter loan 1=yes,0=no',max_value=1,min_value=0)
contact=st.number_input('Enter contact ',max_value=4,min_value=0)
days=st.number_input('Enter days',max_value=31,min_value=1)
month=st.number_input('Enter month ',max_value=12,min_value=1)
duration=st.number_input('Enter duration',min_value=0)
campaign=st.number_input('Enter campaign',min_value=0)
pdays=st.number_input('Enter pdays',min_value=-1)
previous=st.number_input('Enter previous', min_value=0)
poutcome=st.number_input('Enter poutcome 1=yes,0=no',min_value=0)

#load model
model_file=open('random_model.pickle','rb')
model=pickle.load(model_file)

#
def perform_prediction(input_values):
    array_input_value=np.array(input_values)
    reshape_array=array_input_value.reshape(1,-1)
    # perform prediction
    prediction=model.predict(reshape_array)
    #print (prediction)
    
    if prediction[0]==1:
        return 'Yes Subscription'
    else:
        return 'No Subscription'
    
def main():
    
    if st.button('Make Prediction'):
        predict_=perform_prediction([age,job,marital,education,default,balance,housing,loan,contact,days,month,
                                duration,campaign,pdays,previous,poutcome])
        st.success(predict_)

if __name__=='__main__':
    main()
### Introduction
> The project is aimed to predict customer confirming to subscribe to the product marketted by bank call agent
The dataset comprises of six numerical variable and ten categorical variable including the target variable which is yes subscription.
The categorical columns or variable are converted to numerical values using LabelEncoder from scikit-learn preprocessing

### Dataset Cleaning:
There is no significant missing value and duplicated values in the dataset
### Exploratory Data Analysis:
Considering the yes and no subscription which are the label variable are inbalance the average duration of yes subscription and no subscription is 552 and 226 respectively, generally yes subscription has lower data point or value counts compare to no subscription.
The average age to the marital status falls withing 33 and 49 respectively. Looking at the correlation matrix the only significant columns to the target variable is call duration, which implies that calls with high duration or talking length tend to concure to the yes subscription

### Data Preprocessing:
LabelEncoder was use to encode the categoriacal values and pd.map was used to encode the month to maintain its order. The data set is unbalance so random_oversampler was used to balance the dataset.
### Modeling
The data was trained with four different model which are Logistic regression, Decision Tree classifier, RandomForestClassifier and SVC, but the best performning  on both train and test data is RandomForestClassifier with the training accuracy of 100% and test accuracy of 99%

### Model deployment
The application is deployed for better user interaction on streamlit

# Limitation
The dataset contains some outliers which was handled by standardscaler normalization
The dataset is inbalance, this was mannaged by applying randomoversampler to balance it

### Conclussion
The project was an end to end Supervised classification project, which give general overview on bank marketting outcome. 

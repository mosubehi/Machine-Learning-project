# -*- coding: utf-8 -*-
"""FinalProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b9UuNRWFntGmBWx3pk5ztFZSQFa40A_X
"""

#model prediction using RandomForest
from google.colab import drive 
drive.mount('/content/drive/')
import os 
path='/content/drive/My Drive/AI_Lab_144175'
os.chdir(path)

import pandas as pd
import numpy as np
disease=pd.read_csv("diabetes_prediction_dataset.csv")
disease.head()

from sklearn.ensemble import RandomForestRegressor
# Handle duplicates
duplicate_rows_data = disease[disease.duplicated()]
print("number of duplicate rows: ", duplicate_rows_data.shape)
#drop duplicates
disease = disease.drop_duplicates()

#the number of unique values
for column in disease.columns:
    num_distinct_values = len(disease[column].unique())
    print(f"{column}: {num_distinct_values} distinct values")


# Checking null values
print(disease.isnull().sum())

#Categorical encoding (columns with non numerical data)
from sklearn.preprocessing import OrdinalEncoder
columns = ["gender", "smoking_history"]
encoding = OrdinalEncoder()
disease[columns] = encoding.fit_transform(disease[columns])
disease.head()

from sklearn.model_selection import train_test_split
y=disease.diabetes
disease_features = ['gender', 'age', 'hypertension', 'heart_disease', 
                        'smoking_history', 'bmi', 'HbA1c_level','blood_glucose_level']
X = disease[disease_features]
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
preds = forest_model.predict(val_X)
print("mean_absolute_error",mean_absolute_error(val_y,preds))
accuracy = accuracy_score(val_y, preds.round())
print('Accuracy:', accuracy)
print('Accuracy:', int(accuracy*100),"%")

# View confusion matrix for test data and predictions
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
confusion_matrix(val_y, preds.round())

# View the classification report for test data and predictions
print(classification_report(val_y, preds.round()))
import numpy as np
import csv
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('heart.csv')
heartDisease = heartDisease.replace('?',np.nan)

print('Few examples from the dataset are given below')
print(heartDisease.head())

model=BayesianModel([('age','trestbps'),('age','fbs'), ('sex','trestbps'),('exang','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'), ('heartdisease','thalach'),('heartdisease','chol')])

print('\n Learning CPD using Maximum likelihood estimators')
model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)

print('\n Inferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)
print('\n 1. Probability of HeartDisease given Age=50')
q=HeartDisease_infer.query(variables=['heartdisease'],evidence={'age':50})
print(q)

print('\n 2. Probability of HeartDisease given cholesterol=200')
q=HeartDisease_infer.query(variables=['heartdisease'],evidence={'chol':200})
print(q)

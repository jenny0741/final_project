# Heart Disease Prediction Using Machine Learning Model

## Introduction
According to the Mayo Clinic, heart disease can discribe several condition with the heart.  Some of these conditions are coronary 
artery disease (CAD), irregular heartbeats (arrhythmias), birth defects (congenital heart defects), disease of the heart muscle, 
or heart valve disease.  Some of the contributing factors of heart disease are cholesterol deposits (plaques) in the arteries.  These
plaques build up and block the blood flow from the heart.  Some of the symtoms of heart disease can be:
 *  Chest pain, chest tightness, chest pressure and chest discomfort (angina)
 *  Shortness of breath
 *  Pain in the neck, jaw, throat, upper belly area or back
 *  Pain, numbness, weakness or coldness in the legs or arms if the blood vessels in the effect areas are narrowed.
 
 _Source:_  https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118
 
 ## Purpose
 
 Use the dataset from the IEEE DataPort, which include the Cleveland and Hungarian (UCI Machine Learning Repository) to create a machine
 learning anaylysis. These analysis will use the various features of the dataset to predict wheather a patient has a likelihood of having
 a heart attack.   The dataset must first be processed using exploratory data analysis (EDA).   Once the datasets have been cleaned and corrected
 for scale, the diagnosis of heart disease (num) can be accomplished by using different machine learning algorithms.

## Research Question(s)
1. Does the age of the patient contribute to a heart attack?
2. Does the level of blood sugar (FBS) in the patient contribute to a heart attack?
3. Does a higher cholestoral level contribute to a heart attack?
4. Can the level of chest pain be related to the risk of a heart attack?

## Data Source
Data files were sourced from the UCI Machine Learning Repository.   The data files were coverted to csv files and cleaned before analysis.

[Cleaveland dataset csv](Resources/processed_cleveland.csv)

[Hungarian dataset csv](Resources/reprocessed_hungarian.csv)

[VA dataset csv](Resources/processed_va.csv)

_Source_ https://ieee-dataport.org/documents/cardiovascular-disease-dataset

## Dataset Information

 * Age:  Age of Patient
 * Sex:  Sex of Patient
 * cp:  Chest Pain
 * trestbps:  Resting Blood Pressure (in mm Hg)
 * chol:  Serum Cholestoral
 * fbs:  Fasting Blood Sugar
 * restecg:  Resting Electrocardiographic Results
 * thalach:  Maximum Heart Rate Acheived
 * exang:  Exercise Induced Angina (1=yes, 0= no)
 * oldpeak:  ST Depression induced by exercise relative to rest
 * slope:  the slope of the peak exercise ST segment
 * ca:  number of major vessels (1-3)
 * thal: 
 * num:  diagnosis of heart disease
 
 ## Machine Learning Model

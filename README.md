# Heart Disease Prediction Using Machine Learning Model
Presentation Link:

## Introduction
According to the Mayo Clinic, heart disease can describe several conditions with the heart.  Some of these conditions are coronary 
artery disease (CAD), irregular heartbeats (arrhythmias), birth defects (congenital heart defects), disease of the heart muscle, 
or heart valve disease.  Some of the contributing factors of heart disease are cholesterol deposits (plaques) in the arteries.  These
plaques build up and block the blood flow from the heart.  Some of the symtoms of heart disease can be:
 *  Chest pain, chest tightness, chest pressure and chest discomfort (angina)
 *  Shortness of breath
 *  Pain in the neck, jaw, throat, upper belly area or back
 *  Pain, numbness, weakness or coldness in the legs or arms if the blood vessels in the effect areas are narrowed.
 
 _Source:_  https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118
 
 ## Purpose
 
 Use the dataset from the UCI Machine Learning Repository, which include the Cleveland, Hungarian, VA, and Switzerland to create a machine
 learning anaylysis. These analysis will use the various features of the dataset to predict wheather a patient has a likelihood of having
 a heart disease.   The dataset must first be processed using exploratory data analysis (EDA). Once the datasets have been cleaned and corrected
 for scale, the diagnosis of heart disease (num) can be accomplished by using different machine learning algorithms.

## Research Question(s)
1. Does the age of the patient contribute to a heart attack?
2. Does the level of blood sugar (FBS) in the patient contribute to a heart attack?
3. Does a higher cholestoral level contribute to a heart attack?
4. Can the level of chest pain be related to the risk of a heart attack?
5. Does the location of the patient correlate with the risk of heart disease?

## Data Source
Data files were sourced from the UCI Machine Learning Repository.   The dataset were in csv formate which were imported into Pandas for cleaning
before analysis.   The dataset had columns which contained null values.   These columns included ca, thal, and slope   These columns were dopped from all
four datasets.   We also added a columns for location.   Since the datasets were regional, the dataset can be used to further corrolate geogrphical
location with heart disease.

[Cleaveland dataset csv](Resources/processed_cleveland.csv)

[Switzerland dataset csv](Resources/processed_switzerland.csv)

[VA dataset csv](Resources/processed_va.csv)

[Hungarian dataset csv](Resources/reprocessed_hungarian.csv)

_Source_ https://archive.ics.uci.edu/ml/datasets/heart+disease

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
 * slope:  the slope of the peak exercise ST segment DROPPED
 * ca:  number of major vessels (1-3) DROPPED
 * thal: maximum heart rate achieved DROPPED
 * num:  diagnosis of heart disease
 
 ## SQL and Database
 
 [ElephantSQL](Resources/elephant.png)
 
 [DBeaver](Resources/dbeaver.png)
 
 [Server engine link](Resources/server_link.png)
 
 ## Machine Learning Model
 
 The type of machine learning used will be Supervised.   Since the dataset columns were labeled, this gave the ability to use supervised learning to predict
 wheather a patient might or might not have heart disease.   Since the datasets were not continuous, a classification method will be used for predicting a
 discrete outcome.  The first machine learning created for this dataset was deep neural learning.   The accuracy of this model was 19% which is far below
 an acceptable score.   Other learning models would include Decision Tree and Random Forest.
 
 [Deep Neural](Resources/neural.png)
 
 ## Data Visualization
 
 For the data visualization, the program Tableau was chosen.   
 Visualization Link:
 

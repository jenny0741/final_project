# Heart Disease Prediction Using Machine Learning Model
Presentation Link: [Presentation](https://docs.google.com/presentation/d/1vfkKItc84_Lr9fVpbshKxXzubFteUbh5gQcvyLaHr-E/edit?usp=sharing)

## Introduction
According to the Mayo Clinic, heart disease can describe several conditions with the heart.  Some of these conditions are coronary 
artery disease (CAD), irregular heartbeats (arrhythmias), birth defects (congenital heart defects), disease of the heart muscle, 
or heart valve disease.  Some of the contributing factors of heart disease are cholesterol deposits (plaques) in the arteries.  These
plaques build up and block the blood flow from the heart.  Some of the symtoms of heart disease can be:
 *  Chest pain, chest tightness, chest pressure and chest discomfort (angina)
 *  Shortness of breath
 *  Pain in the neck, jaw, throat, upper belly area or back
 *  Pain, numbness, weakness or coldness in the legs or arms if the blood vessels in the effect areas are narrowed.
 
 The CDC website states that heart disease is the leading cause of death in the US. However, with a change in lifestyle, the risk of developing heart disease can be greatly reduced. This is why our group chose this topic. By creating a machine learning tool that can predict heart disease, it would aid in diagnosing patients with heart disease quicker and also to put preventive measures in place prior to diagnosis.
  
 _Source:_  https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118
           https://www.cdc.gov/heartdisease/index.htm
 
 ## Purpose


 Use the dataset from the UCI Machine Learning Repository, which include the Cleveland, Hungarian, VA, and Switzerland to create a machine
 learning anaylysis. These analysis will use the various features of the dataset to predict wheather a patient has a likelihood of having
 a heart disease.   The dataset must first be processed using exploratory data analysis (EDA). Once the datasets have been cleaned and corrected
 for scale, the diagnosis of heart disease (num) can be accomplished by using different machine learning algorithms.

## Research Question(s)
1. Does the age of the patient contribute to heart disease?
2. Does the level of blood sugar (FBS) in the patient contribute to heart disease?
3. Does a higher cholestoral level contribute to heart disease?
4. Can the level of chest pain be related to the risk of heart disease?
5. Does the location of the patient correlate with the risk of heart disease?

## Data Source
Data files were sourced from the UCI Machine Learning Repository.   The dataset were in csv formate which were imported into Pandas for cleaning
before analysis.   The dataset had columns which contained null values.   These columns included ca, thal, and slope   These columns were dopped from all
four datasets.   We also added a columns for location.   Since the datasets were regional, the dataset can be used to further corrolate geogrphical
location with heart disease.

[Cleveland dataset csv](Resources/processed_cleveland.csv)

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
 
 ### ERD
 
 The four datasets in this project were joined with concatenation. The reason for this was the four datasets did not have a single common key feature which related them. Since the data was in the same column names and data type, the datasets were joined using concatenation which simply stacked them into one dataset.
 
 ![image](https://github.com/jenny0741/final_project/blob/main/Resources/erd_heart_disease.png)
 
 ## SQL and Database
 
 [ElephantSQL](Resources/elephant.png)
 
 [DBeaver](Resources/dbeaver.png)
 
 [Server engine link](Resources/server_link.png)
 
 ## Supervised Machine Learning Model
 
 The type of machine learning used will be Supervised.   Since the dataset columns were labeled, this gave the ability to use supervised learning to predict
 wheather a patient might or might not have heart disease.   Since the datasets were not continuous, a classification method will be used for predicting a
 discrete outcome.  
 
 ### Logistic Regression
 
 ![image](https://github.com/jenny0741/final_project/blob/main/Resources/logistic_regression.png)
 
  ### Confusion Matrix for logistic regression
  
  One of the most important classification measures is confusion matrix.  The confusion matrix produces the four important numbers of 
 true positive(TP), true negative (TN), false positive (FP), and flase negative (FN).  These values are used to calculate the accuracy and prec.
 
 ![image](https://github.com/jenny0741/final_project/blob/main/Resources/confusion_matrix.png)
 
  #### Calculating the accuracy:
  
  
  Accuracy = TP + TN / (TP + TN + FP + FN)  **Accuracy of (0) = .75**
  
  
  #### Calculating the precision of (1):
   
  Precision = TP / (TP + FP)  **Precision = .63**
  
  
  #### Calculating the recall of (1):
   
  Recall = TP / (TP + FN)  **Recall = .85**
  
  
  #### Calculating the sensitivity of (1):
   
  Sensitivity = TP / (TP + FN)  **Sensitivity = .53**
  
  
  #### Calculating the F1 score of (1):
   
  F1 score = 2 * (precision * sensitivity)  / (precision + sensitivity)  **F1 score = .58**
  
  #### Classification Report
![image](https://github.com/jenny0741/final_project/blob/main/Resources/classification_matrix.png)
 
 ### Random Forest 
 
![image](https://github.com/jenny0741/final_project/blob/main/Resources/random_forest.png)

 
 ### Neural Network
 
![image](https://github.com/jenny0741/final_project/blob/main/Resources/deep_learnig_layers.png)
 
 
 ## Data Visualization
 
 For the data visualization, the program Tableau was chosen. Two different dashboards will be used to visualize the data. One dashboard will present age demographics data vs. the diagnosis of the patient (heart disease or not). A second  will be used to display gender demographics vs. the diagnosis of the patient. The two will be placed into a storyboard with medical data vs. heart disease visualizations. The story will be used to find and display potential trends that could aid in predicting heart disease in patients. 
 
 Visualization Link: [Visualization](https://public.tableau.com/views/Heart_Disease_Prediction/HeartDiseasePrediction?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)
 

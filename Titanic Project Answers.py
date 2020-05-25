#importing
import numpy as np
import pandas as pd
import visuals as vs
from IPython.display import display
Full_data=pd.read_csv("titanic_data.csv")
display(data.head())
#data Understanding 
Output=data["Survived"]
data=data.drop("Survived", axis =1)
#Predicting

def accuracy_score(x, y):
    """ Returns accuracy score for input truth and predictions. """
    

    if len(x)==len(y):
        
        return "prediction have an accuarcy of {:.2f}%.".format((x==y).mean()*100)
    else:
        return "Number of predictions doesn't match number of output"
    
def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """

    predictions = []
    for _, passenger in data.iterrows():
        
        # Predict the survival of 'passenger'
        predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)

predictions = predictions_0(data)
print(accuracy_score(Output, predictions))#if all predictions are 0 the accuracy is 61.62%
vs.survival_stats(data, Output, 'Pclass')
#Predict that all womans are survived
def predictions_1(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """
    
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex']=="female":
            predictions.append(1)
        else:
            predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_1(data)

#print accuarcy
print(accuracy_score(Output, predictions))#78.68%

#male Scale
vs.survival_stats(data, Output, 'Age', ["Sex == 'male'"])
#Survived passenger was female, then we will predict they survive. If a passenger was male and younger than 10
def predictions_2(data):
    """ Model with two feature: 
            - Predict a passenger survived if they are female & male <10. """
    
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex']=="female" :
            predictions.append(1)
        else:
            if passenger['Age']<10:
                predictions.append(1)
            else:
                predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)
#make the predictions
predictions= predictions_2(data)
#accuray
print(accuracy_score(Output, predictions))#79.35%
#to have 80% accuarcy 
def predictions_3(data):
    """ Model with two feature: 
            - Predict a passenger survived if they are female & male <10. """
    
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex']=="female" or passenger['Fare']>300 :
            predictions.append(1)
        else:
            if passenger['Age']<10 and passenger['Pclass']<3 :
                predictions.append(1)
            else:
                predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)
#predict
predictions= predictions_3(data)
print(accuracy_score(Output, predictions))#>80%
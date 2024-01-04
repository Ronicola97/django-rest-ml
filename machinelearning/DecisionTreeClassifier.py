from sklearn.tree import DecisionTreeClassifier
from joblib import load
import os



def run(name):
    path = os.path.join(os.getcwd(), 'machinelearning', 'arbol.pkl')
    arbol = load(path)
    #test
    y_pred = arbol.predict([[50,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1]])
    print(f'La predicción es: {y_pred}')
    


    
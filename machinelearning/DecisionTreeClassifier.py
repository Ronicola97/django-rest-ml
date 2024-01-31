from sklearn.tree import DecisionTreeClassifier
from joblib import load
import os
from rest_framework.response import Response

def run(data):
    path = os.path.join(os.getcwd(), 'machinelearning', 'dermacan_random_forest.joblib')
    arbol = load(path)
    #test
    #datos_recibidos = [[48,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0]]
    datos_recibidos = data
    y_pred = arbol.predict(datos_recibidos)[0]
    
    if (y_pred == 'Otitis Externa'):
        prob = arbol.predict_proba(datos_recibidos)[0][1]
    elif (y_pred == 'Sarna Sarcoptica'):
        prob = arbol.predict_proba(datos_recibidos)[0][2]
    elif (y_pred == 'Alergia Picadura Pulga'):
        prob = arbol.predict_proba(datos_recibidos)[0][0]
    elif (y_pred == 'Sin enfermedad'):
        prob = arbol.predict_proba(datos_recibidos)[0][3]

    restante = 1-prob;

    return {"prediccion": y_pred, "probabilidad": prob, "restante": restante}
    


    
import pickle
import numpy as np

def pred_loan(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    file = '/Users/malcom/Downloads/Feige/models/clf.sav'
    model = pickle.load(open(file, 'rb'))
    new_user = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9]).reshape(1,-1)
    y_pred = model.predict(new_user)
    if y_pred[0] == 1:
        result = 'eligible'
    else:
        result = 'ineligible'    
    return result
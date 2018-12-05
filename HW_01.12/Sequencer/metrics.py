#metrics of quality library
import numpy as np

def MSE(y_test, y_valid):
    y_test = np.array(y_test)    # преобразуем входной массив в np.массив
    y_valid = np.array(y_valid)
    MSE = 1/len(y_test)*sum((y_test - y_valid)**2)  #np. удобен тем, что производит поэлементные операции без всяких циклов.
    return MSE                         # главное, чтобы массивы были одинаковой длины

def MAE(y_test, y_valid):
    pass     #code this

def RMSE(y_test, y_valid):
    pass   #code this


def ME(y_test, y_valid):
    pass

def SD(y_test, y_valid):
    pass

    

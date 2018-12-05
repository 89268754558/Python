import matplotlib.pyplot as plt 
import numpy as np
import metrics  #Our custom library

# data generator part
x = np.arange(1000)
delta = np.random.uniform(-10,10, size=(len(x),)) # добавим случайный шум ,посмотрите, что лежит внутри
y_test = 0.4 * x +3 + delta   # тестируемая выборка (полученная из эксперимента)
y_valid = 0.4*x + 3    # валидная выборка (правильный ответ без шума)

plt.plot(x,y_test, label = 'Experimental Data')
plt.plot(x, y_valid, label = 'Valid Data')
plt.title('Example of data sample')
plt.legend()
plt.show()

print('Your MSE is : ',metrics.MSE(y_test, y_valid))
#print('Your MAE is : ',metrics.MAE(y_test, y_valid))  #Uncomment this part after compliting metrics.py
#print('Your RMSE is : ',metrics.RMSE(y_test, y_valid))
#print('Your ME is : ',metrics.ME(y_test, y_valid))
#print('Your SD is : ',metrics.MSE(y_test, y_valid))




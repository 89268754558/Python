import random as r  #random library
import numpy as np   #numeric python library
import draw as d   #our custom library

x = np.arange(0,1000)   #generate numpy range between 0 and 1000 (0,1,2,3,4,5,....,999). Last element 999, len(x) = ?
y = r.sample(range(0,1500), 1000)   #generate random range, len(y)= ?


#d.solid_linear(x,y, 'random_variables')  #plot with our custom library. Uncomment this part step-by-step
#d.scatter_linear(x,y, 'random_variables')
#d.combo(x,y, 'random_variables')

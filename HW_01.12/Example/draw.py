#simple drawing example
import matplotlib.pyplot as plt 

def solid_linear(x_array, y_array, title):
    plt.plot(x_array, y_array)
    plt.title(title)
    plt.savefig("%s.png"%title)
    plt.show()

def scatter_linear(x_array, y_array, title):
    plt.scatter(x_array, y_array)
    plt.title(title)
    plt.savefig("%s.png"%title)
    plt.show()

def combo(x_array, y_array, title):
    plt.plot(x_array, y_array, label = 'solid_linear')
    plt.scatter(x_array, y_array, label = 'scatter_linear')
    plt.title(title)
    plt.legend()
    plt.savefig('%s.png'%title)
    plt.show()
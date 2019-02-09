import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine # database connection

from pylab import rcParams
rcParams['figure.figsize'] = 14, 10

def plotter(request):


    disk_engine = create_engine('sqlite:///hh_parse.db') # Initializes database with filename 311_8M.db in current directory
    df = pd.read_sql_query('SELECT salary FROM parseData WHERE lang = "%s"'%(request), disk_engine)

    x = df.salary
    n, bins, patches = plt.hist(x, int(len(x)/2), facecolor='b', alpha=0.6)


    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.title('%s Info: Average Salary = %.1f and STD = %.1f'%(request,x.mean(), x.std()))
    plt.grid(True)
    plt.savefig('%s_plot.png'%request)
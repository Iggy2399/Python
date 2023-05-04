
import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')

mtcars_cyl = mtcars.loc[mtcars['cyl'].isin([4, 6, 8])]

plt.boxplot([mtcars_cyl.loc[mtcars_cyl['cyl'] == 4]['wt'],
             mtcars_cyl.loc[mtcars_cyl['cyl'] == 6]['wt'],
             mtcars_cyl.loc[mtcars_cyl['cyl'] == 8]['wt']])

plt.xticks([1, 2, 3], ['4 CYL', '6 CYL', '8 CYL'])

plt.title('DISTRIBUCIJA TEŽINE AUTOMOBILA PO BROJU CILINDARA')

plt.show()
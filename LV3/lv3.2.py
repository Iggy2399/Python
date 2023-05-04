import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv') # Učitavanje podataka

mtcars_cyl = mtcars.loc[mtcars['cyl'].isin([4, 6, 8])]

mpg_mean = mtcars_cyl.groupby('cyl')['mpg'].mean()

plt.bar(mpg_mean.index, mpg_mean.values)

plt.xlabel('BROJ CYL')
plt.ylabel('POTROŠNJA GORIVA')
plt.title('POTROŠNJA GORIVA PO BROJU CILINDARA')

plt.show()


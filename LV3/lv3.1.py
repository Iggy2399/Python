import pandas as pd
import numpy as np
mtcars = pd.read_csv('mtcars.csv')


print(mtcars.sort_values(by=['mpg']))
mtcars_8 = mtcars[mtcars.cyl == 8]
print(mtcars_8)
mtcars_8_sort = mtcars_8.sort_values(by=['mpg'])
print(mtcars_8_sort)
 
mtcars_6 = mtcars[mtcars.cyl == 6]
mtcars_6_mean = mtcars_6['mpg'].mean()
print(mtcars_6_mean)


mtcars_4 = mtcars[mtcars.cyl == 4]
print(mtcars_4)

mtcars_4_wt = mtcars_4[(mtcars.wt >= 2) & (mtcars.wt <= 2.2)]
print(mtcars_4_wt.mean())


mtcars_auto =mtcars[mtcars.am == 1]
mtcars_manual = mtcars[mtcars.am == 0]

print(mtcars_auto)
print(mtcars_manual)

mtcars_auto_100hp = mtcars_auto[(mtcars.hp > 100)]

print(mtcars_auto_100hp)

mtcars['wt_kg'] = mtcars.wt * 1000 * 0.453592
print(mtcars)

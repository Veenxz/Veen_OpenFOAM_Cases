import pandas as pd
import numpy as np
import os
from glob import glob
from matplotlib import pyplot as plt

os.system('mkdir Data')
rm = glob('Data/*_xy.csv')

for i in rm:
    os.remove(i)

file = 'postProcessing/sixDoFRigidBodyState/0/clean.dat'

# Time          centreOfRotation
df = pd.read_table(file, header=None)

print(df)

print(type(df[0][0]))

df_xy = df[1].str.split(expand=True).astype(float)
df_xy.insert(0, 'Time', df[0])

start = 0
stop = 200
n = 11
time = np.linspace(start, stop, n)
print(time)


for i in range(n-1):
    tem = df_xy.loc[(df_xy['Time'] > time[i]) & (df_xy['Time'] < time[i+1])]
    tem.to_csv('Data/'+str(i)+'_xy.csv', index=False)
    plt.subplot(2, (n-1) / 2, i+1)
    x = tem[0]
    y = tem[1]
    w = 1.0
    titles = "%.0f" % time[i] + " s to " + "%.0f" % time[i+1] + " s"
    plt.plot(x, y, 'r', ls='-', lw=w, c='black')
    plt.xlabel('X', y=-0.0001)
    plt.title(titles, fontsize=10, y=-0.16, c='r')
    plt.ylabel('Y')

# plt.tight_layout()
plt.show()
#pip install pandas#how to install

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data={
'fertilizer':[0,25, 50,75],
'weight':[17,40,70,80]
}

df=pd.DataFrame(data)
print(df)
plt.scatter(df['fertilizer'],df['weight'])
plt.show()
# from matplotlib import pyplot as plt#

# import matplotlib.pyplot as plt

# %matplotlib inline
# import seaborn as sns

# plt.plot (x,y)#standard line plot
# plt.scartter(x,y)#scatter plot

# plt.hisr(x,bins)

plt.bar(df['fertilizer'],df['weight'])

sns.regplot(x='fertilizer',y='weight',data= df)
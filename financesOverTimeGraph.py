import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")


# Creating graph for different financial investments
# constant_rate = np.array([[10,20,30,40,50][1,2,3,4,5]])
# print("cr shape",constant_rate.shape)
rs = np.random.RandomState(365)
values = rs.randn(365, 4).cumsum(axis=0)
dates = pd.date_range("1 1 2016", periods=365, freq="D")
data = pd.DataFrame(values, dates, columns=["Outcome 1", "Outcome 2", "Outcome 3", "Outcome 4"])
data = data.rolling(7).mean()

sns.lineplot(data=data, palette="tab10", linewidth=2.5)

#plot information
plt.title('Performance Over Time') 
plt.ylabel('Dollars in Thousands ($)')
plt.xlabel('Date')

plt.show()
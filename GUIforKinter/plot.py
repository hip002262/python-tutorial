import pandas as pd

import matplotlib.pyplot as plt

def plot_sum_population(df,ax,name,flag,time):
    target_df = df.query('cityname == @name & dayflag == @flag & timezone == @time')
    sum_population_df = target_df[['year_mm', 'population']].groupby('year_mm').sum()

    ax.plot(sum_population_df['population'], label=name)
    plt.legend()


df = pd.read_csv('tokyo.csv')
fig = plt.figure()

ax = fig.add_subplot()
ax.set_xlabel('year')
ax.set_ylabel('population')
plt.xticks(rotation=50)
plot_sum_population(df,ax,'chiyoda',1,0)
plot_sum_population(df,ax,'shinjuku',1,0)
plot_sum_population(df,ax,'taito',1,0)

plt.show()

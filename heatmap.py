import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Vivek Rao\\Desktop\\Academic\\Arnolt Center\\National COVID-19 Tracker\\df.csv')
#df = df[df.columns[::-1]]

#Define the plot
fig, ax = plt.subplots(figsize=(50,33))

#title
title = "Daily change in number of cases, by state"

#edit axes
#ax.tick_params(axis='both', which='major', labelsize=12)
#ax.tick_params(axis='both', which='minor', labelsize=12)

#states
states = pd.read_csv('C:\\Users\\Vivek Rao\\Desktop\\Academic\\Arnolt Center\\National COVID-19 Tracker\\states.csv')
states = states['States'].tolist()

#set font size and title's position from plot
plt.title(title,fontsize=36)
ttl = ax.title
ttl.set_position([0.5,1.05])

sns.heatmap(df,ax=ax,linewidth=0.30,square=True,annot=True,annot_kws={"size":9},fmt="",cmap="YlOrBr",vmin=0,vmax=1000,linecolor='black',yticklabels=states,xticklabels=5,cbar=False)
plt.savefig('C:\\Users\\Vivek Rao\\Desktop\\Academic\\Arnolt Center\\National COVID-19 Tracker\\daily-delta.pdf')

#annot=True,annot_kws={"size":9},fmt="",
#Cases by Metro 4-15.xlsx
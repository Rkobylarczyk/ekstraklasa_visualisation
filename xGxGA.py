import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

table = pd.read_csv("awans4.csv")
table.head()

#Create plot area
#fig, ax = plt.subplots()

#Set plot size
#fig.set_size_inches(7, 5)

#Plot chart as above, but change the plot type from 'o' to '*' - givng us stars!
#plt.plot(table['GF'],table['GA'],"*")

#Add labels to chart area
#ax.set_title("xGoals for & Against")
#ax.set_xlabel("xGoals For")
#ax.set_ylabel("xGoals Against")

fig, ax = plt.subplots()
fig.set_size_inches(7, 5)

plt.plot(table['GF'],table['GA'],"*")
plt.plot([table['GF'].mean(),table['GF'].mean()],[14,5],'k-', linestyle = ":", lw=1)
plt.plot([8,13.5],[table['GA'].mean(),table['GA'].mean()],'k-', linestyle = ":", lw=1)

druzyna = table['Druzyna']
GF = table['GF']
GA = table['GA']

ax.set_title("xGoals For & Against")
ax.set_xlabel("xGoals For")
ax.set_ylabel("xGoals Against")

for i, t in enumerate(druzyna):
    ax.text(GF[i], GA[i], s=str(druzyna[i]))

ax.text(12.25,5.1,"Silny atak, silna obrona",color="red",size="8")
ax.text(8,14,"Słaby atak, słaba obrona",color="red",size="8")

plt.show()

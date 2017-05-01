import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'Algorithms': ['Naive-Bayes', 'Decision Tree', 'Random Forest', 'SVM', 'RankSVM'],
        'Mean Average Precision': [0.211,0.249,0.255,0.270,0.291]}
df = pd.DataFrame(raw_data, columns = ['Algorithms', 'Mean Average Precision'])

# Create the general blog and the "subplots" i.e. the bars
f, ax1 = plt.subplots(1, figsize=(10,5))

# Set the bar width
bar_width = 0.25

# positions of the left bar-boundaries
bar_l = [i+1 for i in range(len(df['Mean Average Precision']))] 

# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i+(bar_width/2) for i in bar_l] 

# Create a bar plot, in position bar_1
barlist = ax1.bar(bar_l,
                  # using the pre_score data
                  df['Mean Average Precision'], 
                  # set the width
                  width=bar_width,
                  alpha=0.5)
    
barlist[0].set_color('r')
barlist[1].set_color('b')
barlist[2].set_color('g')
barlist[3].set_color('y')
barlist[4].set_color('k')
# set the x ticks with names
plt.xticks(tick_pos, df['Algorithms'])

# Set the label and legends
ax1.set_ylabel("Mean Average Precision")
ax1.set_xlabel("Algorithms")
ax1.set_title('Performance')

rects = ax1.patches

# Now make some labels
labels = [0.211,0.249,0.255,0.270,0.291]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, height - 10, label, ha='center', va='bottom')


# Set a buffer around the edge
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])

plt.show()

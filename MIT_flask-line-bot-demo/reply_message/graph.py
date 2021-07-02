import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('Lucia.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

plt.plot(x,y, label='Mean Blood Glucose')
plt.xlabel('Date')
plt.ylabel('Blood Sugar(mg/dL)')
plt.title('Lucia\'s Blood Glucose')
plt.legend()
plt.show()
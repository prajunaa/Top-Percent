import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('insertfile.csv')
fig, ax = plt.subplots()
ax.plot(data["X"], data["Y"], linestyle="-")


def topPercent(data, percent):
    #list of sums of % groups
    sumlist = []
    columnX = data[data.columns[0]]
    columnY = data[data.columns[1]]
    #iterates through every element of the X column
    for i in range(len(columnX)-int(percent*len(columnX))):
        #adds up all the y values for each bundle of certain %, eg if i = 3, it starts at 3 and adds up y values of [3: 3+10% of ColumnX]
        sumY = 0
        for z in columnY[i:int(i+percent*len(columnX))]:
            sumY += z
            sumlist.append((i, int(i+len(columnX)*percent),sumY))
    l=0
    current = [sumlist[0][0],sumlist[0][1]]
    for sum in sumlist:
        b = sum[2]
        if b>l:
            l=b
            current=[sum[0],sum[1]]
    return current

between = topPercent(data,0.25)
print(data['X'][between[0]],data['X'][between[1]])
ax.axvspan(data['X'][between[0]],data['X'][between[1]], color='red', alpha=0.3)
plt.show()

        

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.animation import FuncAnimation



def getDaily(data):
    daily = [0]
    for i in range(1, data.shape[0]):
        daily.append(data['Cases'][i] - data['Cases'][i-1])
    return daily

# data spreadsheet from https://covid19.colorado.gov/data/case-data
data = pd.read_csv('CDPHE_COVID19_Daily_State_Statistics.csv')
data['DailyCases'] = getDaily(data)

# user defined input
COMPARE = 'DailyCases'

# constant(s)
SPEED = 100

# save file as mp4
save = anim.writers['ffmpeg']
s = save(fps = 10, bitrate=1800)


# returns gradient of color according to iteration of animation
def gradient(i):
    step = 1/data.shape[0]
    return (0,1-step*i,step*i)

# returns frame of graph for i iterations through data
def animation(i, compare):
    x = []
    y = []

    x.append(i)
    y.append(data[compare][i])

    graph = plt.bar(x,y, color = gradient(i))
    fig.suptitle('Time Series of COVID-19 ' + str(compare) + '\n' + 'Date: ' + str(data['Date'][i]))

    return graph

fig = plt.figure()

# code for static bars
plt.xlim(0, data.shape[0])
plt.ylim(0,data[COMPARE].max())


# runs through frames documenting each row of data
ani = FuncAnimation(fig, animation, frames = np.arange(data.shape[0]),
                    fargs = (COMPARE,), interval = SPEED, repeat = False)

#ani.save('covid_animation_daily_cases_static_axes.mp4', writer =s)
plt.show()







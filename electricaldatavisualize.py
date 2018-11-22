## https://www.google.com/get/noto/#sans-lgc
from matplotlib import pyplot as plt
from matplotlib import font_manager # for Japanese font
from matplotlib import dates as mdates
import matplotlib.ticker as tick
import numpy as np
import datetime
import pandas as pd
import matplotlib
rowdata = pd.read_excel('electricdata_aug.xlsx')

#print(rowdata)

file = rowdata.iloc[:, [8, 10, 12, 14]]
print(file.index[0], file.index[len(file)-1])
#print(file.index.values)
x1 = file.index.values
y1 = file.iloc[:,0]#'[TR-1]主電動機消費電力（瞬時）[kW]']
y2 = file.iloc[:,1]#'[TR-2]主電動機消費電力（瞬時）[kW]']
y3 = file.iloc[:,2]#'[TR-3]主電動機消費電力（瞬時）[kW]']
y4 = file.iloc[:,3]#'[TR-4]主電動機消費電力（瞬時）[kW]']

# # file.plot(x=x1)
#
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.plot(x1, y4)
print(file.index[0])
#file.plot()
plt.xlim(xmin=file.index[0], xmax=file.index[len(file)-1])
#plt.xticks(np.arange(0, 7*24, 4))
plt.ylim(ymin=0.0)
#plt.gac().set_xticklabels(('2017-07-03T00:00:00.000000000', '2017-07-03T06:30:00.000000000', '285', '290', '295',  '300',  '305',  '310', '315'))
font = font_manager.FontProperties(family='AppleGothic')  # cann't find noto sans cjk jp


plt.legend(loc='lower right', prop=font)


plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d  '))
#
# ax = plt.subplot(111)
# # Shrink current axis's height by 10% on the bottom
# box = ax.get_position()
# ax.set_position([box.x0, box.y0 + box.height * 0.1,
#                  box.width, box.height * 0.9])
# # Put a legend below current axis
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
#           fancybox=True, shadow=True, ncol=5)

hoursLoc = mdates.HourLocator(interval=12) #为6小时为1副刻度
plt.gca().xaxis.set_minor_locator(hoursLoc)
plt.gca().xaxis.set_minor_formatter(mdates.DateFormatter('%H'))
plt.xlabel("Date")
plt.ylabel("Electrical Consume")
plt.grid(True)
plt.show()

one_day = pd.read_csv('power-demand-day.csv')
xx = one_day.columns.values
yy = one_day.iloc[4:8,1:].values
print(yy)
yy1 = yy[0,:]
yy2 = yy[1,:]
yy3 = yy[2,:]
yy4 = yy[3,:]
print(xx[1:])
print(yy1)
p1, = plt.plot(yy1)
p2, = plt.plot(yy2)
p3, = plt.plot(yy3)
p4, = plt.plot(yy4)
plt.xlim(xmin=0,xmax=23)
plt.xticks(np.arange(0,24,4))
plt.axes().xaxis.set_minor_locator(tick.MultipleLocator(1))
plt.xlabel("Hour")
plt.ylabel("Electrical(10^4Kw)")
plt.legend([p1,p2,p3,p4],['2001年度(7月)','2010年度(7月)','2015年度(8月)','2016年度(8月)'],prop=font)
plt.grid(b=True,which='minor')
plt.grid()
plt.show()



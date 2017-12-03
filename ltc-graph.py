import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime
import time

up = True
first_run = True

inv_val = 100.00
inv_price = 4175.00

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

data_points = 0;

def animate(i):
    global first_run
    global data_points
    if not first_run:
	limits = plt.axis()
    pullData = open("ltc-GBP.txt","r").read()
    dataArray = pullData.split('\n')
    dataArray.pop()
    xar = []
    yar = []
    z = 1
    for eachLine in dataArray:
        if len(eachLine)>1:
            splt = eachLine.split(':')
            #form_date = datetime.datetime.fromtimestamp(float(splt[0])).strftime('%Y-%m-%d %H:%M:%S')
            #form_date = datetime.datetime.fromtimestamp(float(splt[0])).strftime('%Y-%m-%d %H:%M:%S')
            #xar.append(str(form_date))
            xar.append(z)
            yar.append(round(float(splt[1])))
            z = z + 1
    ax1.clear()
    ax1.plot(xar,yar)
    if not first_run:
    	plt.axis(limits)
    else:
	limits = plt.axis()
	first_run = False

    if len(dataArray)>data_points:
        data_points = len(dataArray)
        print "Updated"
    #plt.axis([xmin,xmax,ymin,ymax])
    #plt.axis([1000,1400,4100,4900])

    if yar[-1]<yar[-2]:
    	plt.title("vCur:"+str(yar[-1])+" - Min:"+str(min(yar))+" - Prof:"+str(round((inv_val/inv_price)*yar[-1]-100)))
    else:
	plt.title("^Cur:"+str(yar[-1])+" - Min:"+str(min(yar))+" - Prof:"+str(round((inv_val/inv_price)*yar[-1]-100)))

'''
aa = open("GBP.txt","r").read().split("\n")
aa.pop()
bb = []
for cc in aa:
    dd = cc.split(":")
    bb.append(float(dd[3]))
    print dd[3]'''

ani = animation.FuncAnimation(fig, animate, interval=10000)
plt.show()

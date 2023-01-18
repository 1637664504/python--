import matplotlib.pyplot as plt

#公式生成 数列2
x=range(1,20)
y=[a**2 for a in x]

plt.style.use('seaborn')
fig,axes = plt.subplots()
axes.scatter(x,y,s=10,c=y,cmap=plt.cm.Blues) #c=(红,绿,蓝)
plt.show()
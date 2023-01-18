import matplotlib.pyplot as plt

#公式生成 数列1
i=[a for a in range(1,10)]
j=[2*a for a in range(1,10)]

#公式生成 数列2
x=range(1,10)
y=[a**2 for a in x]

plt.style.use('seaborn')
fig,axes = plt.subplots()
axes.scatter(i,j,s=10,c='red')  #红
axes.scatter(x,y,s=10,c=(0,0.8,0)) #c=(红,绿,蓝)
plt.show()
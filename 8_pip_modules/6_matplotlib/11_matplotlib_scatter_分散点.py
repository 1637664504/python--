import matplotlib.pyplot as plt
#公式生成 数列

# x=[a for a in range(1,10)]
# y=[2*a for a in range(1,10)]

x=range(1,100)
y=[a**2 for a in x]

plt.style.use('seaborn')
fig,axes = plt.subplots()
axes.scatter(x,y,s=10)  #s=10 设置点大小
plt.show()
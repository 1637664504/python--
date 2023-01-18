import matplotlib.pyplot as plt
#公式生成 数列
ax_x=[1,2,3,4,5]
ax_y=[1,4,9,16,25]
plt.style.use('seaborn')
fig,axes = plt.subplots()
axes.plot(ax_x,ax_y)
plt.show()